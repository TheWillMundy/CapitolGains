"""Tests for scraper.py module."""

import os
import pytest
from pathlib import Path
from capitolgains.utils.scraper import HouseDisclosureScraper

@pytest.fixture(scope="function")
def scraper():
    """Create a HouseDisclosureScraper instance for testing."""
    with HouseDisclosureScraper(headless=False) as s:
        yield s

@pytest.fixture(scope="function")
def temp_download_dir(tmp_path_factory):
    """Create a temporary directory for downloads."""
    return tmp_path_factory.mktemp("downloads")

class TestScraperBasics:
    """Basic functionality tests for HouseDisclosureScraper."""

    def test_scraper_initialization(self):
        """Test basic scraper initialization."""
        scraper = HouseDisclosureScraper()
        assert scraper._headless is True
        assert scraper._playwright is None
        assert scraper._browser is None
        assert scraper._context is None
        assert scraper._page is None

    def test_scraper_context_management(self):
        """Test scraper context management."""
        with HouseDisclosureScraper(headless=False) as scraper:
            assert scraper._playwright is not None
            assert scraper._browser is not None
            assert scraper._context is not None
            assert scraper._page is not None
            assert scraper.BASE_URL == "https://disclosures-clerk.house.gov/FinancialDisclosure"

    def test_get_available_years(self, scraper):
        """Test retrieving available years for financial disclosures."""
        years = scraper.get_available_years()
        assert isinstance(years, list)
        assert len(years) > 0
        assert all(year.isdigit() for year in years)
        assert int(years[0]) >= 2024  # Most recent year first
        assert years == sorted(years, reverse=True)  # Verify sorted order

class TestDisclosureSearch:
    """Tests for disclosure search functionality."""

    def test_search_member_disclosures_basic(self, scraper):
        """Test basic disclosure search functionality."""
        results = scraper.search_member_disclosures(
            last_name="Pelosi",
            filing_year="2024"
        )
        
        assert isinstance(results, list)
        if results:
            self._verify_disclosure_structure(results[0])

    def test_search_member_disclosures_with_state(self, scraper):
        """Test searching with state specification."""
        results = scraper.search_member_disclosures(
            last_name="Pelosi",
            filing_year="2024",
            state="CA"
        )
        
        assert isinstance(results, list)
        if results:
            assert all('CA' in r['office'] for r in results)

    def test_search_member_disclosures_with_district(self, scraper):
        """Test searching with district specification."""
        results = scraper.search_member_disclosures(
            last_name="Pelosi",
            filing_year="2024",
            state="CA",
            district="12"  # Pelosi's current district after redistricting
        )
        
        assert isinstance(results, list)
        if results:
            # Check that all results are for CA and either district 11 (old) or 12 (new)
            assert all(
                'CA' in r['office'] and 
                any(f'-{d}' in r['office'] for d in ['11', '12'])
                for r in results
            )

    @staticmethod
    def _verify_disclosure_structure(disclosure):
        """Helper to verify disclosure structure."""
        assert 'name' in disclosure
        assert 'office' in disclosure
        assert 'year' in disclosure
        assert 'filing_type' in disclosure
        assert 'pdf_url' in disclosure
        assert any(code in disclosure['filing_type'] for code in ['PTR', 'FD'])

class TestFileDownloads:
    """Tests for file download functionality."""

    def test_download_disclosure_pdf(self, scraper, temp_download_dir):
        """Test downloading a specific disclosure PDF."""
        results = scraper.search_member_disclosures(
            last_name="Pelosi",
            filing_year="2024",
            state="CA"
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

    def test_download_annual_report(self, scraper, temp_download_dir):
        """Test downloading an annual report ZIP file."""
        years = scraper.get_available_years()
        test_year = years[0]
        
        zip_path = scraper.download_annual_report(
            year=test_year,
            download_dir=str(temp_download_dir)
        )
        
        assert os.path.exists(zip_path)
        assert zip_path.endswith('.zip')
        assert os.path.getsize(zip_path) > 0