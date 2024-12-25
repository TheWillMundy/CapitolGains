"""House financial disclosure scraper.

This module provides functionality to scrape financial disclosures from the House of
Representatives website. It handles searching for disclosures, downloading PDFs, and
retrieving annual reports.

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

class HouseDisclosureScraper:
    """Scraper for House of Representatives financial disclosures.
    
    This class provides methods to:
    - Search for member disclosures by name, year, state, and district
    - Download individual disclosure PDFs
    - Download annual disclosure report archives
    - Retrieve available years for financial disclosures
    
    The scraper uses Playwright for reliable browser automation and includes
    proper error handling and retry logic for network operations.
    
    Attributes:
        BASE_URL: Base URL for the House Financial Disclosure portal
        _headless: Whether to run browser in headless mode
        _playwright: Playwright instance
        _browser: Browser instance
        _context: Browser context
        _page: Current page
    """
    
    BASE_URL = "https://disclosures-clerk.house.gov/FinancialDisclosure"
    MAX_RETRIES = 3
    RETRY_DELAY = 2  # seconds
    
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
        
    def __enter__(self):
        """Start Playwright when entering context.
        
        Returns:
            Self for context manager usage.
            
        Note:
            This sets up the browser with appropriate configurations for
            reliable scraping of the House website.
        """
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(headless=self._headless)
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
            
    def _safe_get_cell_text(self, cell) -> str:
        """Safely get text from a table cell, handling None cases.
        
        Args:
            cell: The table cell element or None
            
        Returns:
            The cell's text content or empty string if cell is None
        """
        if cell is None:
            return ""
        return cell.inner_text().strip()
    
    def _safe_get_cell_link(self, cell) -> Optional[str]:
        """Safely get link from a table cell, handling None cases.
        
        Args:
            cell: The table cell element or None
            
        Returns:
            The href attribute of the first link in the cell, or None if no link exists
        """
        if cell is None:
            return None
            
        link = cell.query_selector('a')
        if link is None:
            return None
            
        href = link.get_attribute('href')
        if not href:
            return None
            
        return href
            
    def search_member_disclosures(
        self,
        last_name: str,
        filing_year: str,
        state: Optional[str] = None,
        district: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Search for a specific member's financial disclosures.
        
        This method navigates to the search page, fills out the form, and extracts
        disclosure information from the results table. It includes retry logic for
        reliability.
        
        Args:
            last_name: Member's last name
            filing_year: Year to search for
            state: Optional two-letter state code
            district: Optional district number
            
        Returns:
            List of dictionaries containing disclosure information:
            [
                {
                    'name': str,
                    'office': str (format: "STATE-DISTRICT"),
                    'year': str,
                    'filing_type': str,
                    'pdf_url': Optional[str]
                },
                ...
            ]
            
        Raises:
            TimeoutError: If the search results don't load within the timeout period
            ValueError: If the search form cannot be submitted
        """
        logger.info(f"Searching for disclosures - Name: {last_name}, Year: {filing_year}")
        
        for attempt in range(self.MAX_RETRIES):
            try:
                self._page.goto(self.BASE_URL)
                
                # Wait for and click search tab
                search_tab = self._page.wait_for_selector('a[href="#Search"]', timeout=15000)
                search_tab.click()
                
                # Wait for form and fill it out
                self._page.wait_for_selector('.search-filter, #searchForm', state='visible', timeout=15000)
                self._page.fill('#LastName', last_name)
                time.sleep(1)  # Small delay for stability
                self._page.select_option('#FilingYear', filing_year)
                
                if state:
                    self._page.select_option('#State', state)
                    time.sleep(1)
                    
                if district:
                    self._page.fill('#District', district)
                
                # Submit and wait for results
                submit_button = self._page.query_selector('button[type="submit"]')
                submit_button.click()
                
                # Wait for either results or no results message
                self._page.wait_for_selector(
                    '#DataTables_Table_0_wrapper, .alert-info',
                    state='visible',
                    timeout=20000
                )
                
                # Check for no results
                no_results = self._page.query_selector('.alert-info')
                if no_results and "No results found" in no_results.inner_text():
                    return []
                    
                # Wait for table to fully load
                self._page.wait_for_selector('#DataTables_Table_0_info', state='visible', timeout=15000)
                
                # Extract results
                results = []
                rows = self._page.query_selector_all('#DataTables_Table_0 tbody tr')
                
                for row in rows:
                    try:
                        name_cell = row.query_selector('td[data-label="Name"]')
                        office_cell = row.query_selector('td[data-label="Office"]')
                        year_cell = row.query_selector('td[data-label="Filing Year"]')
                        filing_cell = row.query_selector('td[data-label="Filing"]')
                        
                        pdf_url = self._safe_get_cell_link(name_cell)
                        if not pdf_url:
                            continue
                            
                        # Ensure proper URL formatting
                        if pdf_url.startswith('/'):
                            full_pdf_url = f"https://disclosures-clerk.house.gov{pdf_url}"
                        else:
                            full_pdf_url = f"https://disclosures-clerk.house.gov/{pdf_url}"
                            
                        result = {
                            'name': self._safe_get_cell_text(name_cell),
                            'office': self._safe_get_cell_text(office_cell),
                            'year': self._safe_get_cell_text(year_cell),
                            'filing_type': self._safe_get_cell_text(filing_cell),
                            'pdf_url': full_pdf_url
                        }
                        
                        if all(result.values()):
                            results.append(result)
                            
                    except Exception as e:
                        logger.warning(f"Error processing row: {str(e)}")
                        continue
                        
                return results
                
            except PlaywrightTimeout as e:
                if attempt == self.MAX_RETRIES - 1:
                    raise TimeoutError("Search results did not load within timeout period") from e
                logger.warning(f"Timeout on attempt {attempt + 1}, retrying...")
                time.sleep(self.RETRY_DELAY)
                
            except Exception as e:
                if attempt == self.MAX_RETRIES - 1:
                    raise ValueError(f"Failed to search disclosures: {str(e)}") from e
                logger.warning(f"Error on attempt {attempt + 1}, retrying...")
                time.sleep(self.RETRY_DELAY)
        
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
            
        # Ensure URL starts with base URL and has proper formatting
        if not pdf_url.startswith("https://disclosures-clerk.house.gov"):
            if pdf_url.startswith('/'):
                pdf_url = f"https://disclosures-clerk.house.gov{pdf_url}"
            else:
                pdf_url = f"https://disclosures-clerk.house.gov/{pdf_url}"
            
        for attempt in range(self.MAX_RETRIES):
            try:
                logger.info(f"Downloading PDF from {pdf_url}")
                
                # Set headers for PDF download
                headers = {
                    "Accept": "application/pdf",
                    "Content-Type": "application/pdf"
                }
                self._page.set_extra_http_headers(headers)
                
                # Get the filename from the URL
                filename = os.path.basename(pdf_url)
                download_path = os.path.join(download_dir, filename)
                
                # Download the file directly using Playwright's request API
                response = self._page.request.get(pdf_url)
                if response.status != 200:
                    raise ValueError(f"Failed to download PDF: HTTP {response.status}")
                    
                # Save the file
                with open(download_path, 'wb') as f:
                    f.write(response.body())
                    
                # Verify the download
                if not os.path.exists(download_path) or os.path.getsize(download_path) == 0:
                    raise ValueError("Downloaded PDF is empty or does not exist")
                    
                return download_path
                
            except Exception as e:
                if attempt == self.MAX_RETRIES - 1:
                    raise ValueError(f"Failed to download PDF: {str(e)}") from e
                logger.warning(f"Download failed on attempt {attempt + 1}, retrying...")
                time.sleep(self.RETRY_DELAY)
            
    def get_available_years(self) -> List[str]:
        """Get list of available years for financial disclosures.
        
        Returns:
            List of years as strings, sorted with most recent first
            
        Note:
            This method scrapes the years from the financial disclosure downloads section
            of the website.
        """
        self._page.goto(self.BASE_URL)
        self._page.wait_for_selector('div.panel.library-panel#download', timeout=10000)
        years = []
        
        # Find all year links in the financial disclosure downloads section
        year_links = self._page.query_selector_all('div.col-md-12 a')
        for link in year_links:
            year_text = link.inner_text().strip()
            if year_text.isdigit():  # Only include actual years
                years.append(year_text)
                
        return sorted(years, reverse=True)  # Most recent first
        
    def download_annual_report(self, year: str, download_dir: Optional[str] = None) -> str:
        """Download the annual financial disclosure report for a given year.
        
        Args:
            year: The year to download (e.g., "2024")
            download_dir: Optional directory to save the file. If None, uses a temp directory.
            
        Returns:
            Path to the downloaded ZIP file
            
        Raises:
            ValueError: If the download fails or the file is invalid
        """
        if not download_dir:
            download_dir = tempfile.mkdtemp()
            
        for attempt in range(self.MAX_RETRIES):
            try:
                self._page.goto(self.BASE_URL)
                
                # Wait for the downloads section
                self._page.wait_for_selector(
                    'div.col-md-12 h2:has-text("DOWNLOAD FINANCIAL DISCLOSURE REPORTS BY YEAR")', 
                    timeout=10000
                )
                
                # Find and get the download URL
                year_link = self._page.query_selector(f'a:has-text("{year}")')
                if not year_link:
                    raise ValueError(f"No report available for year {year}")
                    
                href = year_link.get_attribute('href')
                download_url = f"https://disclosures-clerk.house.gov{href}"
                
                # Setup download path
                download_path = os.path.join(download_dir, f"{year}FD.zip")
                
                # Download with proper headers
                self._page.set_extra_http_headers({
                    "Accept": "application/zip",
                    "Content-Type": "application/zip"
                })
                
                # Download the file
                with open(download_path, 'wb') as f:
                    response = self._page.request.get(download_url)
                    f.write(response.body())
                    
                # Verify the download
                if not os.path.exists(download_path) or os.path.getsize(download_path) == 0:
                    raise ValueError("Downloaded ZIP file is empty or does not exist")
                    
                return download_path
                
            except Exception as e:
                if attempt == self.MAX_RETRIES - 1:
                    raise ValueError(f"Failed to download ZIP file: {str(e)}") from e
                logger.warning(f"Download failed on attempt {attempt + 1}, retrying...")
                time.sleep(self.RETRY_DELAY) 