"""Tests for senator_scraper.py module."""

import logging
import os
import pytest
from pathlib import Path
from capitolgains.utils.senator_scraper import SenateDisclosureScraper

# Add logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Ensure all loggers propagate to root
logging.getLogger('capitolgains').setLevel(logging.DEBUG)
logging.getLogger('capitolgains.utils.senate_scraper').setLevel(logging.DEBUG)

@pytest.fixture(scope="function")
def scraper():
    """Create a SenateDisclosureScraper instance for testing.
    
    Uses non-headless mode to help with debugging.
    """
    with SenateDisclosureScraper(headless=False) as s:
        yield s

@pytest.fixture(scope="function")
def temp_download_dir(tmp_path_factory):
    """Create a temporary directory for downloads."""
    return tmp_path_factory.mktemp("downloads")

class TestScraperBasics:
    """Basic functionality tests for SenateDisclosureScraper."""

    def test_scraper_initialization(self):
        """Test basic scraper initialization."""
        scraper = SenateDisclosureScraper()
        assert scraper._headless is True
        assert scraper._playwright is None
        assert scraper._browser is None
        assert scraper._context is None
        assert scraper._page is None

    def test_scraper_context_management(self):
        """Test scraper context management."""
        with SenateDisclosureScraper(headless=False) as scraper:
            assert scraper._playwright is not None
            assert scraper._browser is not None
            assert scraper._context is not None
            assert scraper._page is not None
            assert scraper.BASE_URL == "https://efdsearch.senate.gov"

    def test_agreement_acceptance(self, scraper):
        """Test accepting the initial agreement."""
        # First acceptance
        scraper._accept_agreement()
        assert scraper._page.url == f"{scraper.BASE_URL}/search/"
        assert scraper._agreement_accepted is True
        
        # Second acceptance should skip
        initial_url = scraper._page.url
        scraper._accept_agreement()
        assert scraper._page.url == initial_url  # URL shouldn't change
        assert scraper._agreement_accepted is True
        
    def test_agreement_persistence(self, scraper):
        """Test that agreement acceptance persists within a session."""
        # Accept agreement initially
        scraper._accept_agreement()
        assert scraper._agreement_accepted is True
        
        # Navigate to a different page
        scraper._page.goto(f"{scraper.BASE_URL}/search/home/")
        
        # Agreement should still be considered accepted
        assert scraper._agreement_accepted is True
        
        # Accepting again should be a no-op
        scraper._accept_agreement()
        assert scraper._agreement_accepted is True

    def test_report_type_mapping(self):
        """Test report type mapping constants."""
        scraper = SenateDisclosureScraper()
        assert 'annual' in scraper.REPORT_TYPE_MAP
        assert 'ptr' in scraper.REPORT_TYPE_MAP
        assert 'extension' in scraper.REPORT_TYPE_MAP
        assert 'blind_trust' in scraper.REPORT_TYPE_MAP
        assert 'other' in scraper.REPORT_TYPE_MAP

class TestDisclosureSearch:
    """Tests for disclosure search functionality."""

    def test_search_member_disclosures_basic(self, scraper):
        """Test basic disclosure search functionality."""
        results = scraper.search_member_disclosures(
            last_name="Warren",
            filing_year="2024"
        )
        
        assert isinstance(results, list)
        if results:
            self._verify_disclosure_structure(results[0])

    def test_search_member_disclosures_with_state(self, scraper):
        """Test searching with state specification."""
        results = scraper.search_member_disclosures(
            last_name="Warren",
            filing_year="2023",
            state="MA"
        )
        
        assert isinstance(results, list)
        if results:
            assert all(
                r['first_name'].lower() == 'elizabeth' and 
                r['last_name'].lower() == 'warren'
                for r in results
            )

    def test_search_member_disclosures_with_first_name(self, scraper):
        """Test searching with first name specification."""
        results = scraper.search_member_disclosures(
            last_name="Warren",
            first_name="Elizabeth",
            filing_year="2024"
        )
        
        assert isinstance(results, list)
        if results:
            assert all(
                r['first_name'].lower() == 'elizabeth' and 
                r['last_name'].lower() == 'warren'
                for r in results
            )

    def test_search_member_disclosures_with_report_types(self, scraper):
        """Test searching with specific report types."""
        results = scraper.search_member_disclosures(
            last_name="Warren",
            filing_year="2024",
            report_types=['ptr']
        )
        
        assert isinstance(results, list)
        if results:
            assert all('periodic transaction' in r['report_type'].lower() for r in results)

    def test_pagination_handling(self, scraper):
        """Test handling of paginated results."""
        # Use a senator known to have many disclosures
        results = scraper.search_member_disclosures(
            last_name="Tuberville",
            filing_year="2023"
        )
        
        # Verify we got results from multiple pages
        assert len(results) > 25  # Default page size is 25
        
        # Verify all results have consistent structure
        for result in results:
            self._verify_disclosure_structure(result)

    def test_search_with_multiple_report_types(self, scraper):
        """Test searching with multiple report types."""
        results = scraper.search_member_disclosures(
            last_name="Warren",
            filing_year="2024",
            report_types=['annual', 'ptr', 'extension']
        )
        
        assert isinstance(results, list)
        if results:
            report_types = {r['report_type'].lower() for r in results}
            assert any('annual' in rt or 'periodic' in rt or 'extension' in rt for rt in report_types)

    @staticmethod
    def _verify_disclosure_structure(disclosure):
        """Helper to verify disclosure structure."""
        assert 'first_name' in disclosure
        assert 'last_name' in disclosure
        assert 'office' in disclosure
        assert 'report_type' in disclosure
        assert 'date' in disclosure
        assert 'pdf_url' in disclosure
        assert disclosure['pdf_url'].startswith('https://efdsearch.senate.gov')

class TestFileDownloads:
    """Tests for file download functionality."""

    def test_download_disclosure_pdf(self, scraper, temp_download_dir):
        """Test downloading a specific disclosure PDF."""
        results = scraper.search_member_disclosures(
            last_name="Warren",
            filing_year="2024",
            state="MA"
        )
        
        result = next((r for r in results if r['pdf_url']), None)
        if result:
            pdf_path = scraper.download_disclosure_pdf(
                result['pdf_url'],
                download_dir=str(temp_download_dir)
            )
            
            assert os.path.exists(pdf_path)
            assert pdf_path.endswith('.pdf')
            assert os.path.getsize(pdf_path) > 0
            
            # Verify file permissions
            assert os.access(pdf_path, os.R_OK)

class TestErrorHandling:
    """Tests for error handling and edge cases."""

    def test_invalid_search_parameters(self, scraper):
        """Test handling of invalid search parameters."""
        results = scraper.search_member_disclosures(
            last_name="NonexistentPerson",
            filing_year="2024"
        )
        assert isinstance(results, list)
        assert len(results) == 0

    def test_invalid_pdf_url(self, scraper, temp_download_dir):
        """Test handling of invalid PDF URL."""
        with pytest.raises(ValueError, match="Failed to download PDF"):
            scraper.download_disclosure_pdf(
                "https://efdsearch.senate.gov/nonexistent.pdf",
                download_dir=str(temp_download_dir)
            )
            
    def test_retry_behavior(self, scraper):
        """Test retry behavior on network issues."""
        # Force a timeout by using an invalid domain
        with pytest.raises(Exception):
            scraper._page.goto("https://invalid.domain.test", timeout=100)