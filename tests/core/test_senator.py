"""Tests for senator.py module."""

import logging
import os
from datetime import datetime
import pytest
from capitolgains.core.senator import Senator
from capitolgains.utils.senate_scraper import SenateDisclosureScraper

# Test Data
CURRENT_YEAR = str(datetime.now().year)
TEST_YEAR = CURRENT_YEAR

# Add logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Ensure all loggers propagate to root
logging.getLogger('capitolgains').setLevel(logging.DEBUG)
logging.getLogger('capitolgains.utils.senate_scraper').setLevel(logging.DEBUG)
logging.getLogger('capitolgains.core.senator').setLevel(logging.DEBUG)

@pytest.fixture(scope="function")
def scraper():
    """Create a SenateDisclosureScraper instance for testing."""
    with SenateDisclosureScraper(headless=False) as s:
        yield s

@pytest.fixture(scope="function")
def temp_download_dir(tmp_path_factory):
    """Create a temporary directory for downloads."""
    return tmp_path_factory.mktemp("downloads")

@pytest.fixture(scope="function")
def warren():
    """Create a test senator for Elizabeth Warren."""
    return Senator("Warren", first_name="Elizabeth", state="MA")

@pytest.fixture(scope="function")
def tuberville():
    """Create a test senator for Tommy Tuberville."""
    return Senator("Tuberville", first_name="Tommy", state="AL")

# Unit Tests
class TestSenatorUnit:
    """Unit tests for Senator class."""
    
    def test_initialization_with_all_params(self):
        """Test initialization with all parameters."""
        sen = Senator("Warren", first_name="Elizabeth", state="MA")
        assert sen.name == "Warren"
        assert sen.first_name == "Elizabeth"
        assert sen.state == "MA"
        assert isinstance(sen._cached_disclosures, dict)
        assert len(sen._cached_disclosures) == 0
    
    def test_initialization_minimal(self):
        """Test initialization with only required parameters."""
        sen = Senator("Warren")
        assert sen.name == "Warren"
        assert sen.first_name is None
        assert sen.state is None
    
    def test_disclosure_caching(self, scraper, warren):
        """Test that disclosures are properly cached."""
        first_result = warren.get_disclosures(scraper, year=TEST_YEAR)
        assert TEST_YEAR in warren._cached_disclosures
        
        second_result = warren.get_disclosures(scraper, year=TEST_YEAR)
        assert first_result is second_result  # Should be same object (cached)
        
    def test_matches_senator_case_insensitive(self):
        """Test case-insensitive name matching."""
        sen = Senator("WARREN", first_name="ELIZABETH", state="MA")
        disclosure = {
            'first_name': 'Elizabeth',
            'last_name': 'Warren',
            'office': 'MA'
        }
        assert sen._matches_senator(disclosure)

# Integration Tests
class TestSenatorIntegration:
    """Integration tests for Senator class with scraper."""
    
    def test_disclosure_retrieval_and_categorization(self, scraper, warren):
        """Test disclosure retrieval, filtering, and categorization."""
        disclosures = warren.get_disclosures(scraper, year=TEST_YEAR)
        
        # Check basic structure
        assert isinstance(disclosures, dict)
        assert 'trades' in disclosures
        assert 'annual' in disclosures
        assert 'blind_trust' in disclosures
        assert 'extension' in disclosures
        assert 'other' in disclosures
        
        # Verify all results are for the correct senator
        all_results = []
        for category in disclosures.values():
            all_results.extend(category)
            
        if all_results:
            for result in all_results:
                assert result['first_name'].lower() == 'elizabeth'
                assert result['last_name'].lower() == 'warren'
                assert 'MA' in result['office']
                assert 'report_type' in result
                assert 'pdf_url' in result
                assert result['pdf_url'] is not None
                
                # Check filing type categorization
                report_type = result['report_type'].lower()
                if result in disclosures['trades']:
                    assert 'periodic transaction' in report_type
                elif result in disclosures['annual']:
                    assert 'annual' in report_type
                elif result in disclosures['blind_trust']:
                    assert 'blind trust' in report_type
                elif result in disclosures['extension']:
                    assert 'extension' in report_type
                else:
                    assert result in disclosures['other']
                    
    def test_pdf_download(self, scraper, warren, temp_download_dir):
        """Test PDF download functionality."""
        disclosures = warren.get_disclosures(scraper, year=TEST_YEAR)
        
        # Try to download a PDF if available
        for category in disclosures.values():
            if category:
                disclosure = category[0]
                if disclosure['pdf_url']:
                    file_path = scraper.download_disclosure_pdf(
                        disclosure['pdf_url'],
                        download_dir=str(temp_download_dir)
                    )
                    assert os.path.exists(file_path)
                    assert os.path.getsize(file_path) > 0
                    assert os.access(file_path, os.R_OK)
                    break

    def test_get_recent_trades(self, scraper, tuberville):
        """Test retrieving recent trades using a senator known for frequent trading."""
        trades = tuberville.get_recent_trades(scraper, year=TEST_YEAR)
        assert isinstance(trades, list)
        if trades:
            for trade in trades:
                assert 'periodic transaction' in trade['report_type'].lower()
                assert trade['pdf_url'] is not None
                assert trade['first_name'].lower() == 'tommy'
                assert trade['last_name'].lower() == 'tuberville'

    def test_get_annual_disclosure(self, scraper, warren):
        """Test retrieving annual disclosure."""
        try:
            disclosure = warren.get_annual_disclosure(scraper, int(TEST_YEAR))
            assert 'annual' in disclosure['report_type'].lower()
            assert disclosure['pdf_url'] is not None
            assert disclosure['first_name'].lower() == 'elizabeth'
            assert disclosure['last_name'].lower() == 'warren'
            if 'file_path' in disclosure:
                assert os.path.exists(disclosure['file_path'])
                assert os.path.getsize(disclosure['file_path']) > 0
        except ValueError:
            # Early in the year, annual disclosure might not be available
            pass
            
    def test_multiple_years(self, scraper, warren):
        """Test retrieving disclosures from multiple years."""
        current_year = int(TEST_YEAR)
        years = [str(year) for year in range(current_year - 2, current_year)]
        
        for year in years:
            disclosures = warren.get_disclosures(scraper, year=year)
            assert isinstance(disclosures, dict)
            assert year in warren._cached_disclosures

# Edge Cases
class TestSenatorEdgeCases:
    """Test edge cases and error handling."""
        
    def test_no_results_found(self, scraper):
        """Test handling when no results are found."""
        sen = Senator("NonexistentPerson", state="FL")
        disclosures = sen.get_disclosures(scraper, year=TEST_YEAR)
        assert len(disclosures['trades']) == 0
        assert len(disclosures['annual']) == 0
        assert len(disclosures['blind_trust']) == 0
        assert len(disclosures['extension']) == 0
        assert len(disclosures['other']) == 0

    def test_name_matching(self, scraper):
        """Test name matching with different cases."""
        sen = Senator("WARREN", first_name="ELIZABETH", state="MA")
        disclosures = sen.get_disclosures(scraper, year=TEST_YEAR)
        
        all_results = []
        for category in disclosures.values():
            all_results.extend(category)
            
        if all_results:
            for result in all_results:
                assert result['first_name'].lower() == 'elizabeth'
                assert result['last_name'].lower() == 'warren'
                
    def test_invalid_year(self, scraper, warren):
        """Test handling of invalid year."""
        with pytest.raises(ValueError):
            warren.get_annual_disclosure(scraper, 1900)  # Too old
            
    def test_future_year(self, scraper, warren):
        """Test handling of future year."""
        future_year = str(int(TEST_YEAR) + 2)
        disclosures = warren.get_disclosures(scraper, year=future_year)
        assert all(len(category) == 0 for category in disclosures.values()) 