"""Senate financial disclosure scraper.

This module provides functionality to scrape financial disclosures from the Senate
website. It handles searching for disclosures, downloading PDFs, and retrieving
annual reports.

The scraper uses Playwright for browser automation, with proper resource management
through context managers. It includes proper error handling for network operations.
"""

import os
import time
import logging
from pathlib import Path
import tempfile
from typing import List, Optional, Dict, Any, Tuple, Union
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
    - Process both web table and PDF filings
    
    The scraper handles the Senate's specific requirements, such as accepting
    the initial agreement and managing the DataTables-based results interface.
    
    Attributes:
        BASE_URL: Base URL for the Senate Financial Disclosure portal
        SEARCH_PATH: Path to the search page
    """
    
    BASE_URL = "https://efdsearch.senate.gov"
    SEARCH_PATH = "/search/"
    
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
        self._session_start_time = None
        
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
            
    def with_session(self, target_url: Optional[str] = None, force_new: bool = False) -> 'SenateDisclosureScraper':
        """Ensure a valid Senate session exists.
        
        This method ensures we have an active session with the Senate disclosure site,
        handling the agreement acceptance if needed. It can either reuse an existing
        session or create a new one.
        
        Args:
            target_url: Optional URL to navigate to (defaults to search page)
            force_new: Whether to force a new session even if one exists
            
        Returns:
            Self for method chaining
            
        Raises:
            TimeoutError: If unable to establish session
        """
        session_age = time.time() - (self._session_start_time or 0) if self._session_start_time else None
        
        if force_new:
            logger.info("Forcing new session")
        elif not self._agreement_accepted:
            logger.info("Starting new session (agreement not accepted)")
        elif target_url:
            logger.info(f"Navigating to new page within session (age: {session_age:.1f}s)")
        else:
            logger.info(f"Reusing existing session (age: {session_age:.1f}s)")
            
        if force_new or not self._agreement_accepted:
            self._accept_agreement(target_url)
            self._session_start_time = time.time()
        elif target_url:  # Have session but want different page
            self._page.goto(target_url)
            self._page.wait_for_load_state('networkidle')
        return self

    def _accept_agreement(self, target_url: Optional[str] = None):
        """Accept the initial agreement on the Senate disclosure site.
        
        This is required before any operations can be performed.
        The Senate site requires explicit acceptance of terms via a checkbox.
        
        Args:
            target_url: Optional URL to navigate to after accepting agreement.
                       If None, defaults to the search page.
        
        Raises:
            TimeoutError: If the agreement page doesn't load or accept within timeout
        """
        try:
            # Default to search page if no target URL provided
            target_url = target_url or f"{self.BASE_URL}{self.SEARCH_PATH}"
            
            # Always navigate to target URL first
            self._page.goto(target_url)
            self._page.wait_for_load_state('networkidle')
            
            # Check if we need to accept agreement by looking for the form
            agreement_form = self._page.query_selector('#agreement_form')
            if agreement_form:
                logger.debug("Found agreement form, accepting")
                # We're on the agreement page, need to accept
                self._page.click('#agree_statement')
                self._page.wait_for_url(target_url, timeout=5000)
                self._agreement_accepted = True
            else:
                # We're already on the target page
                logger.debug("No agreement form found, already on target page")
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
        """Wait forDataTable results to load completely."""
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
            
            # Detailed table inspection
            table_info = self._page.evaluate('''() => {
                const table = document.querySelector('#filedReports');
                if (!table) return { exists: false };
                
                const headers = Array.from(table.querySelectorAll('thead th'))
                    .map(th => th.innerText.trim());
                    
                const tbody = table.querySelector('tbody');
                const rows = tbody ? Array.from(tbody.querySelectorAll('tr')) : [];
                
                return {
                    exists: true,
                    headers: headers,
                    rowCount: rows.length,
                    firstRowCells: rows.length > 0 ? 
                        Array.from(rows[0].querySelectorAll('td'))
                            .map(td => td.innerText.trim()) : [],
                    html: table.outerHTML.substring(0, 500) // First 500 chars for debugging
                };
            }''')
            
            logger.debug(f"Table inspection results: {table_info}")
            
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
        report_types: Optional[List[str]] = None,
        include_candidate_reports: bool = False
    ) -> List[Dict[str, Any]]:
        """Search for a specific senator's financial disclosures.
        
        This method handles the complete search process:
        1. Ensures we have a valid session
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
            include_candidate_reports: Whether to include candidate reports in results
            
        Returns:
            List of dictionaries containing disclosure information
            
        Raises:
            TimeoutError: If the search results don't load within timeout period
            ValueError: If the search form cannot be submitted or results cannot be processed
        """
        try:
            logger.debug(f"Starting search for {first_name} {last_name}, {state}, year {filing_year}")
            # Ensure we have a valid session on the search page
            self.with_session(f"{self.BASE_URL}{self.SEARCH_PATH}")
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
            
            logger.debug("Form filled with basic info")
            
            # Select senator type and state if provided
            self._page.check('.senator_filer')
            if state:
                self._page.select_option('#senatorFilerState', state)
                logger.debug(f"Selected state: {state}")
            
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
                logger.debug(f"Selected report types: {report_types}")
            
            # Submit search and wait for results
            logger.debug("Submitting search form")
            self._page.click('button[type="submit"]')
            
            has_results = self._wait_for_results_loading()
            logger.debug(f"Search results loaded, has_results: {has_results}")
            
            if not has_results:
                logger.debug("No results found")
                return []
            
            # Extract results from all pages
            all_results = []
            page_num = 1
            
            while True:
                logger.debug(f"Processing page {page_num}")
                results = self._extract_page_results()
                logger.debug(f"Found {len(results)} results on page {page_num}")
                all_results.extend(results)
                
                # Check for next page
                next_button = self._page.query_selector('.paginate_button.next:not(.disabled)')
                if not next_button:
                    logger.debug("No more pages")
                    break
                    
                # Load next page
                next_button.click()
                self._wait_for_results_loading()
                page_num += 1
            
            # Filter out candidate reports if not wanted
            if not include_candidate_reports:
                all_results = [
                    r for r in all_results 
                    if 'candidate' not in r['report_type'].lower()
                ]
                
            logger.debug(f"Total results found: {len(all_results)}")
            return all_results
                
        except PlaywrightTimeout as e:
            raise TimeoutError("Search results did not load within timeout period") from e
        except Exception as e:
            raise ValueError(f"Failed to search disclosures: {str(e)}") from e

    def _extract_page_results(self) -> List[Dict[str, Any]]:
        """Extract disclosure information from the current results page.
        
        Processes each row in the results table to extract disclosure details.
        Ensures URLs are properly formatted with the base URL if needed.
        
        Returns:
            List of dictionaries containing disclosure information from current page.
        """
        results = []
        rows = self._page.query_selector_all('#filedReports tbody tr')
        logger.debug(f"Found {len(rows)} rows in table")
        
        for i, row in enumerate(rows):
            try:
                cells = row.query_selector_all('td')
                logger.debug(f"Row {i + 1} has {len(cells)} cells")
                
                if len(cells) < 5:  # Skip malformed rows
                    logger.warning(f"Row {i + 1} has insufficient cells: {len(cells)}")
                    continue
                    
                report_cell = cells[3]
                report_link = report_cell.query_selector('a')
                if not report_link:  # Skip rows without report links
                    logger.warning(f"Row {i + 1} has no report link")
                    continue
                    
                # Extract disclosure information
                result = {
                    'first_name': cells[0].inner_text().strip(),
                    'last_name': cells[1].inner_text().strip(),
                    'office': cells[2].inner_text().strip(),
                    'report_type': report_cell.inner_text().strip(),
                    'date': cells[4].inner_text().strip(),
                    'report_url': report_link.get_attribute('href')  # Renamed from pdf_url
                }
                
                logger.debug(f"Extracted result from row {i + 1}: {result}")
                
                # Ensure proper URL formatting
                if result['report_url'] and result['report_url'].startswith('/'):
                    result['report_url'] = f"{self.BASE_URL}{result['report_url']}"
                    
                results.append(result)
                
            except Exception as e:
                logger.warning(f"Error processing row {i + 1}: {str(e)}")
                continue
                
        return results
        
    def download_disclosure_pdf(self, pdf_url: str, download_dir: Optional[str] = None) -> str:
        """Download a specific disclosure PDF.
        
        Args:
            pdf_url: URL of the filing to download
            download_dir: Optional directory to save the file. If None, uses a temp directory.
            
        Returns:
            Path to the downloaded/generated PDF file
            
        Raises:
            ValueError: If the download/generation fails or the PDF is invalid
        """
        if not download_dir:
            download_dir = tempfile.mkdtemp()
            
        try:
            # Process the filing and get the PDF path
            result = self.process_filing(pdf_url, download_dir)
            if not result['file_path']:
                raise ValueError("Failed to get PDF file path")
            return result['file_path']
                
        except Exception as e:
            raise ValueError(f"Failed to download/generate PDF: {str(e)}") from e
            
    def _determine_filing_type(self, report_url: str) -> str:
        """Determine whether a filing is a web table or PDF.
        
        This method navigates to the report URL and checks the page structure
        to determine if it's a web table or PDF filing.
        
        Args:
            report_url: URL of the report to check
            
        Returns:
            'web_table' or 'pdf' indicating the filing type
        """
        try:
            self._page.goto(report_url)
            self._page.wait_for_load_state('networkidle')
            
            # Check for web table
            web_table = self._page.query_selector('#reportDataTable')
            if web_table:
                return 'web_table'
                
            # If no web table, assume it's a PDF filing
            return 'pdf'
            
        except Exception as e:
            logger.warning(f"Error determining filing type: {str(e)}")
            return 'pdf'  # Default to PDF on error
            
    def _generate_pdf(self, download_dir: str) -> str:
        """Generate a PDF from the current page.
        
        Args:
            download_dir: Directory to save the PDF
            
        Returns:
            Path to the generated PDF file
        """
        # Generate unique filename
        timestamp = int(time.time())
        pdf_path = os.path.join(download_dir, f"report_{timestamp}.pdf")
        
        # Generate PDF using Playwright's PDF function
        self._page.pdf(path=pdf_path, format='Letter')
        
        if not os.path.exists(pdf_path) or os.path.getsize(pdf_path) == 0:
            raise ValueError("Generated PDF is empty or does not exist")
            
        return pdf_path
            
    def _scrape_web_table(self, report_url: str) -> Dict[str, Any]:
        """Scrape data from a web table filing.
        
        Args:
            report_url: URL of the web table report
            
        Returns:
            Dictionary containing the parsed web table data
        """
        try:
            self._page.goto(report_url)
            self._page.wait_for_selector('#reportDataTable', state='visible', timeout=10000)
            
            # Extract table data using JavaScript for better performance
            table_data = self._page.evaluate('''() => {
                const tables = Array.from(document.querySelectorAll('#reportDataTable'));
                return tables.map(table => {
                    const headers = Array.from(table.querySelectorAll('thead th'))
                        .map(th => th.innerText.trim().toLowerCase());
                        
                    const rows = Array.from(table.querySelectorAll('tbody tr'))
                        .map(row => {
                            const cells = Array.from(row.querySelectorAll('td'));
                            return Object.fromEntries(
                                headers.map((header, i) => [header, cells[i]?.innerText?.trim() || ''])
                            );
                        });
                        
                    return {
                        headers: headers,
                        rows: rows
                    };
                });
            }''')
            
            if not table_data:
                raise ValueError("Failed to extract web table data")
                
            return {
                'type': 'web_table',
                'tables': table_data
            }
            
        except Exception as e:
            raise ValueError(f"Failed to scrape web table: {str(e)}") from e
            
    def process_filing(self, report_url: str, download_dir: Optional[str] = None) -> Dict[str, Any]:
        """Process a filing, handling both web tables and PDFs.
        
        This method:
        1. Determines if the filing is a web table or PDF
        2. Routes to appropriate handler
        3. Returns structured data and/or file paths
        
        Args:
            report_url: URL of the report to process
            download_dir: Optional directory for saving files
            
        Returns:
            Dictionary containing:
            - 'type': 'web_table' or 'pdf'
            - 'data': Parsed data for web tables
            - 'file_path': Path to PDF file
        """
        if not download_dir:
            download_dir = tempfile.mkdtemp()
            
        filing_type = self._determine_filing_type(report_url)
        logger.debug(f"Processing {filing_type} filing from {report_url}")
        
        if filing_type == 'web_table':
            # First get the full report PDF
            pdf_path = None
            try:
                # Look for printer-friendly version
                printer_link = self._page.query_selector('a[href*="print"]:has-text("Printer-Friendly")')
                if printer_link:
                    # Store current URL to return to later
                    current_url = self._page.url
                    
                    # Get printer-friendly URL and navigate to it
                    printer_url = printer_link.get_attribute('href')
                    if printer_url.startswith('/'):
                        printer_url = f"{self.BASE_URL}{printer_url}"
                    
                    logger.debug(f"Navigating to printer-friendly version: {printer_url}")    
                    # Navigate to printer-friendly version
                    self._page.goto(printer_url)
                    self._page.wait_for_load_state('networkidle')
                    
                    # Generate PDF from the printer-friendly page
                    pdf_path = self._generate_pdf(download_dir)
                    logger.debug(f"Generated PDF at: {pdf_path}")
                    
                    # Return to original page
                    self._page.goto(current_url)
                    self._page.wait_for_load_state('networkidle')
                    
            except Exception as e:
                logger.warning(f"Failed to generate PDF from web table: {str(e)}")
                
            # Then scrape the web tables
            data = self._scrape_web_table(report_url)
            
            return {
                'type': 'web_table',
                'data': data,
                'file_path': pdf_path
            }
            
        else:  # PDF filing
            try:
                # Look for printer-friendly version with more flexible selector
                printer_link = self._page.query_selector('a[href*="/print/"]:has-text("Printer-Friendly"), a.btn-primary:has-text("Printer-Friendly")')
                if not printer_link:
                    raise ValueError("No printer-friendly version found for PDF filing")
                
                # Store current URL to return to later
                current_url = self._page.url
                
                # Get printer-friendly URL and navigate to it
                printer_url = printer_link.get_attribute('href')
                if printer_url.startswith('/'):
                    printer_url = f"{self.BASE_URL}{printer_url}"
                
                logger.debug(f"Navigating to printer-friendly version: {printer_url}")    
                # Navigate to printer-friendly version
                self._page.goto(printer_url)
                self._page.wait_for_load_state('networkidle')
                
                # Generate PDF from the printer-friendly page
                pdf_path = self._generate_pdf(download_dir)
                logger.debug(f"Generated PDF at: {pdf_path}")
                
                # Return to original page
                self._page.goto(current_url)
                self._page.wait_for_load_state('networkidle')
                
                return {
                    'type': 'pdf',
                    'data': None,
                    'file_path': pdf_path
                }
                    
            except Exception as e:
                raise ValueError(f"Failed to generate PDF: {str(e)}") from e 