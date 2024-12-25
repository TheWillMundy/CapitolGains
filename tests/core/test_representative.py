"""Tests for representative.py module."""

import os
from datetime import datetime
import pytest
from capitolgains.core.representative import Representative
from capitolgains.utils.scraper import HouseDisclosureScraper

# Test Data
CURRENT_YEAR = str(datetime.now().year)
TEST_YEAR = CURRENT_YEAR

@pytest.fixture(scope="function")
def scraper():
    """Create a HouseDisclosureScraper instance for testing."""
    with HouseDisclosureScraper(headless=False) as s:
        yield s

@pytest.fixture(scope="function")
def temp_download_dir(tmp_path_factory):
    """Create a temporary directory for downloads."""
    return tmp_path_factory.mktemp("downloads")

@pytest.fixture(scope="function")
def pelosi():
    """Create a test representative for Pelosi."""
    return Representative("Pelosi", state="CA", district="11")

# Unit Tests
class TestRepresentativeUnit:
    """Unit tests for Representative class."""
    
    def test_initialization_with_all_params(self):
        """Test initialization with all parameters."""
        rep = Representative("Pelosi", state="CA", district="11")
        assert rep.name == "Pelosi"
        assert rep.state == "CA"
        assert rep.district == "11"
        assert isinstance(rep._cached_disclosures, dict)
        assert len(rep._cached_disclosures) == 0
    
    def test_initialization_minimal(self):
        """Test initialization with only required parameters."""
        rep = Representative("Pelosi")
        assert rep.name == "Pelosi"
        assert rep.state is None
        assert rep.district is None
    
    def test_disclosure_caching(self, scraper):
        """Test that disclosures are properly cached."""
        rep = Representative("Pelosi", state="CA", district="11")
        
        first_result = rep.get_disclosures(scraper, year=TEST_YEAR)
        assert TEST_YEAR in rep._cached_disclosures
        
        second_result = rep.get_disclosures(scraper, year=TEST_YEAR)
        assert first_result is second_result  # Should be same object (cached)

# Integration Tests
class TestRepresentativeIntegration:
    """Integration tests for Representative class with scraper."""
    
    def test_disclosure_retrieval_and_categorization(self, scraper, pelosi):
        """Test disclosure retrieval, filtering, and categorization."""
        disclosures = pelosi.get_disclosures(scraper, year=TEST_YEAR)
        
        # Check basic structure
        assert isinstance(disclosures, dict)
        assert 'trades' in disclosures
        assert 'annual' in disclosures
        
        # Verify all results are for the correct representative
        all_results = disclosures['trades'] + disclosures['annual']
        if all_results:
            for result in all_results:
                assert "CA-11" in result['office']
                assert "PELOSI" in result['name'].upper()
                assert 'filing_type' in result
                assert 'pdf_url' in result
                assert result['pdf_url'] is not None
                
                # Check filing type categorization
                if result in disclosures['trades']:
                    assert 'PTR' in result['filing_type']
                else:
                    assert 'FD' in result['filing_type']
    
    def test_pdf_download(self, scraper, pelosi, temp_download_dir):
        """Test PDF download functionality."""
        disclosures = pelosi.get_disclosures(scraper, year=TEST_YEAR)
        
        # Try to download a PDF if available
        for category in ['annual', 'trades']:
            if disclosures[category]:
                disclosure = disclosures[category][0]
                if disclosure['pdf_url']:
                    file_path = scraper.download_disclosure_pdf(disclosure['pdf_url'])
                    assert os.path.exists(file_path)
                    assert os.path.getsize(file_path) > 0
                    break

    def test_get_recent_trades(self, scraper, pelosi):
        """Test retrieving recent trades."""
        trades = pelosi.get_recent_trades(scraper, year=TEST_YEAR)
        assert isinstance(trades, list)
        if trades:
            for trade in trades:
                assert 'PTR' in trade['filing_type']
                assert trade['pdf_url'] is not None

    def test_get_annual_disclosure(self, scraper, pelosi):
        """Test retrieving annual disclosure."""
        try:
            disclosure = pelosi.get_annual_disclosure(scraper, int(TEST_YEAR))
            assert 'FD' in disclosure['filing_type']
            assert disclosure['pdf_url'] is not None
            if 'file_path' in disclosure:
                assert os.path.exists(disclosure['file_path'])
        except ValueError:
            # Early in the year, annual disclosure might not be available
            pass

# Edge Cases
class TestRepresentativeEdgeCases:
    """Test edge cases and error handling."""
        
    def test_no_results_found(self, scraper):
        """Test handling when no results are found."""
        rep = Representative("NonexistentPerson", state="FL", district="1")
        disclosures = rep.get_disclosures(scraper, year=TEST_YEAR)
        assert len(disclosures['trades']) == 0
        assert len(disclosures['annual']) == 0 