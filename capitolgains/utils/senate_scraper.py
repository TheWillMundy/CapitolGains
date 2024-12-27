"""Senate financial disclosure scraper.

This module provides functionality to scrape financial disclosures from the Senate
website. It handles searching for disclosures, downloading PDFs, and retrieving
annual reports.

The scraper uses Playwright for browser automation, with proper resource management
through context managers. It includes retry logic and proper error handling for
network operations.
"""

import os
import time
import logging
from pathlib import Path
import tempfile
from typing import List, Optional, Dict, Any
from playwright.sync_api import sync_playwright, Page, Browser, TimeoutError as PlaywrightTimeout

# Configure logging
logger = logging.getLogger(__name__)

class SenateDisclosureScraper:
    """Scraper for Senate financial disclosures.
    
    This class provides methods to:
    - Search for senator disclosures by name, year, and state
    - Download individual disclosure PDFs
    - Handle pagination through search results
    - Manage browser automation with proper error handling
    
    The scraper handles the Senate's specific requirements, such as accepting
    the initial agreement and managing the DataTables-based results interface.
    
    Attributes:
        BASE_URL: Base URL for the Senate Financial Disclosure portal
        MAX_RETRIES: Maximum number of retry attempts for network operations
        RETRY_DELAY: Delay between retry attempts in seconds
    """
    
    BASE_URL = "https://efdsearch.senate.gov"
    MAX_RETRIES = 3
    RETRY_DELAY = 1
    
    # Map of report types to their form values
    REPORT_TYPE_MAP = {
        'annual': '7',
        'ptr': '11',
        'extension': '10',
        'blind_trust': '14',
        'other': '15'
    }
    
    def __init__(self, headless: bool = True):
        """Initialize the scraper with a Playwright instance.
        
        Args:
            headless: Whether to run the browser in headless mode. Defaults to True.
                     Set to False for debugging and development.
        """
        self._headless = headless
        self._playwright = None
        self._browser = None
        self._context = None
        self._page = None
        self._agreement_accepted = False
        
    def __enter__(self):
        """Start Playwright when entering context.
        
        Returns:
            Self for context manager usage.
        """
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(
            headless=self._headless,
            args=['--disable-dev-shm-usage']  # Improve performance
        )
        self._context = self._browser.new_context(
            viewport={'width': 1280, 'height': 800},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'
        )
        self._page = self._context.new_page()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up Playwright resources when exiting context."""
        if self._page:
            self._page.close()
        if self._context:
            self._context.close()
        if self._browser:
            self._browser.close()
        if self._playwright:
            self._playwright.stop()
            
    def _accept_agreement(self):
        """Accept the initial agreement on the Senate disclosure site.
        
        This is required before any search operations can be performed.
        The Senate site requires explicit acceptance of terms via a checkbox.
        If the agreement has already been accepted in this session, this
        method will skip the acceptance process.
        
        Raises:
            TimeoutError: If the agreement page doesn't load or accept within timeout
        """
        try:
            # Always navigate to search page first
            self._page.goto(f"{self.BASE_URL}/search/")
            self._page.wait_for_load_state('networkidle')
            
            # Check if we need to accept agreement by looking for the form
            agreement_form = self._page.query_selector('#agreement_form')
            if agreement_form:
                logger.debug("Found agreement form, accepting")
                # We're on the agreement page, need to accept
                self._page.click('#agree_statement')
                self._page.wait_for_url(f"{self.BASE_URL}/search/", timeout=5000)
                self._agreement_accepted = True
            else:
                # We're already on the search page
                logger.debug("No agreement form found, already on search page")
                self._agreement_accepted = True
            
        except PlaywrightTimeout as e:
            raise TimeoutError("Failed to accept agreement") from e
            
    def _wait_for_search_form(self):
        """Wait for the search form to be loaded and ready.
        
        This ensures all form elements are present and interactive before
        attempting to fill them. Uses a single JavaScript evaluation for
        efficiency in checking multiple elements.
        
        Raises:
            Exception: If required form elements are missing or not interactive
        """
        try:
            # Wait for main form container
            self._page.wait_for_selector('#searchForm', state='visible', timeout=5000)
            
            # Check all required form elements in one operation
            self._page.evaluate('''() => {
                const required = {
                    'Form container': '#searchForm',
                    'Filer types section': '#filerTypesDiv',
                    'Report types section': '#reportTypesDiv',
                    'First name field': '#firstName',
                    'Last name field': '#lastName',
                    'Senator checkbox': '.senator_filer',
                    'State dropdown': '#senatorFilerState'
                };
                
                const missing = Object.entries(required)
                    .filter(([_, selector]) => !document.querySelector(selector))
                    .map(([name]) => name);
                    
                if (missing.length) {
                    throw new Error(`Missing required elements: ${missing.join(', ')}`);
                }
                
                // Verify form is interactive
                document.getElementById('lastName').focus();
            }''')
            
        except Exception as e:
            raise ValueError(f"Search form not ready: {str(e)}") from e
            
    def _wait_for_results_loading(self):
        """Wait for DataTable results to load completely.
        
        The Senate site uses DataTables which shows a processing indicator
        while loading. This method ensures we properly wait for the complete
        loading cycle.
        
        Returns:
            bool: True if results were found, False if no results
        """
        try:
            # Wait for processing to start
            self._page.wait_for_selector(
                '#filedReports_processing',
                state='visible',
                timeout=5000
            )
            
            # Wait for processing to complete
            self._page.wait_for_selector(
                '#filedReports_processing',
                state='hidden',
                timeout=10000
            )
            
            # Wait for either results or no results message
            self._page.wait_for_selector(
                '#filedReports tbody tr, .alert-info',
                state='visible',
                timeout=5000
            )
            
            # Check for no results message
            no_results = self._page.query_selector('.alert-info')
            if no_results and "No results found" in no_results.inner_text():
                return False
                
            # Verify we have actual result rows
            return bool(self._page.query_selector_all('#filedReports tbody tr'))
            
        except PlaywrightTimeout as e:
            raise TimeoutError("Results did not load within timeout period") from e
            
    def search_member_disclosures(
        self,
        last_name: str,
        filing_year: str,
        first_name: Optional[str] = None,
        state: Optional[str] = None,
        report_types: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Search for a specific senator's financial disclosures.
        
        This method handles the complete search process:
        1. Accepts the initial agreement if needed
        2. Fills out the search form with provided criteria
        3. Handles the DataTables loading states
        4. Extracts results across all pagination pages
        
        Args:
            last_name: Senator's last name
            filing_year: Year to search for
            first_name: Optional first name for more specific searches
            state: Optional two-letter state code
            report_types: Optional list of report types to search for
                        ('annual', 'ptr', 'extension', 'blind_trust', 'other')
            
        Returns:
            List of dictionaries containing disclosure information:
            [
                {
                    'first_name': str,
                    'last_name': str,
                    'office': str,
                    'report_type': str,
                    'date': str,
                    'pdf_url': str
                },
                ...
            ]
            
        Raises:
            TimeoutError: If the search results don't load within timeout period
            ValueError: If the search form cannot be submitted
        """
        for attempt in range(self.MAX_RETRIES):
            try:
                # Ensure we're on search page with agreement accepted
                self._accept_agreement()
                self._wait_for_search_form()
                
                # Fill form using efficient JavaScript evaluation
                self._page.evaluate('''([lastName, firstName]) => {
                    const ln = document.getElementById('lastName');
                    const fn = document.getElementById('firstName');
                    ln.value = lastName;
                    if (firstName) fn.value = firstName;
                    
                    // Clear any existing report type selections
                    document.querySelectorAll('input[name="report_type"]')
                        .forEach(el => el.checked = false);
                }''', [last_name, first_name])
                
                # Select senator type and state if provided
                self._page.check('.senator_filer')
                if state:
                    self._page.select_option('#senatorFilerState', state)
                
                # Select report types if specified
                if report_types:
                    selectors = [
                        f'input[name="report_type"][value="{self.REPORT_TYPE_MAP[rt]}"]'
                        for rt in report_types if rt in self.REPORT_TYPE_MAP
                    ]
                    if selectors:
                        self._page.evaluate(
                            'selectors => selectors.forEach(s => document.querySelector(s).checked = true)',
                            selectors
                        )
                
                # Submit search and wait for results
                self._page.click('button[type="submit"]')
                if not self._wait_for_results_loading():
                    return []
                
                # Extract results from all pages
                all_results = []
                page_num = 1
                
                while True:
                    results = self._extract_page_results()
                    all_results.extend(results)
                    
                    # Check for next page
                    next_button = self._page.query_selector('.paginate_button.next:not(.disabled)')
                    if not next_button:
                        break
                        
                    # Load next page
                    next_button.click()
                    self._wait_for_results_loading()
                    page_num += 1
                
                return all_results
                
            except Exception as e:
                if attempt == self.MAX_RETRIES - 1:
                    raise
                time.sleep(self.RETRY_DELAY)
                
    def _extract_page_results(self) -> List[Dict[str, Any]]:
        """Extract disclosure information from the current results page.
        
        Processes each row in the results table to extract disclosure details.
        Ensures URLs are properly formatted with the base URL if needed.
        
        Returns:
            List of dictionaries containing disclosure information from current page.
        """
        results = []
        rows = self._page.query_selector_all('#filedReports tbody tr')
        
        for row in rows:
            try:
                cells = row.query_selector_all('td')
                if len(cells) < 5:  # Skip malformed rows
                    continue
                    
                report_cell = cells[3]
                report_link = report_cell.query_selector('a')
                if not report_link:  # Skip rows without report links
                    continue
                    
                # Extract disclosure information
                result = {
                    'first_name': cells[0].inner_text().strip(),
                    'last_name': cells[1].inner_text().strip(),
                    'office': cells[2].inner_text().strip(),
                    'report_type': report_cell.inner_text().strip(),
                    'date': cells[4].inner_text().strip(),
                    'pdf_url': report_link.get_attribute('href')
                }
                
                # Ensure proper URL formatting
                if result['pdf_url'] and result['pdf_url'].startswith('/'):
                    result['pdf_url'] = f"{self.BASE_URL}{result['pdf_url']}"
                    
                results.append(result)
                
            except Exception as e:
                logger.warning(f"Error processing row: {str(e)}")
                continue
                
        return results
        
    def download_disclosure_pdf(self, pdf_url: str, download_dir: Optional[str] = None) -> str:
        """Download a specific disclosure PDF.
        
        Args:
            pdf_url: URL of the PDF to download
            download_dir: Optional directory to save the file. If None, uses a temp directory.
            
        Returns:
            Path to the downloaded file
            
        Raises:
            ValueError: If the download fails or the PDF is invalid
        """
        if not download_dir:
            download_dir = tempfile.mkdtemp()
            
        for attempt in range(self.MAX_RETRIES):
            try:
                # Set headers for PDF download
                self._page.set_extra_http_headers({
                    "Accept": "application/pdf",
                    "Content-Type": "application/pdf"
                })
                
                # Get filename from URL and ensure .pdf extension
                filename = os.path.basename(pdf_url)
                if not filename.endswith('.pdf'):
                    filename = f"{filename}.pdf"
                download_path = os.path.join(download_dir, filename)
                
                # Download and verify file
                response = self._page.request.get(pdf_url)
                if response.status != 200:
                    raise ValueError(f"Failed to download PDF: HTTP {response.status}")
                    
                with open(download_path, 'wb') as f:
                    f.write(response.body())
                    
                if not os.path.exists(download_path) or os.path.getsize(download_path) == 0:
                    raise ValueError("Downloaded PDF is empty or does not exist")
                    
                return download_path
                
            except Exception as e:
                if attempt == self.MAX_RETRIES - 1:
                    raise ValueError(f"Failed to download PDF: {str(e)}") from e
                time.sleep(self.RETRY_DELAY) 