"""Tests for scraper utility functions."""
import pytest
from pathlib import Path
from capitolgains.utils.senator_scraper import SenateDisclosureScraper
from capitolgains.utils.representative_scraper import HouseDisclosureScraper

@pytest.mark.scraper
def test_senate_scraper_initialization(senate_scraper):
    """Test Senate scraper initialization."""
    assert isinstance(senate_scraper, SenateDisclosureScraper)
    assert hasattr(senate_scraper, 'driver')
    assert hasattr(senate_scraper, 'wait')

@pytest.mark.scraper
def test_house_scraper_initialization(house_scraper):
    """Test House scraper initialization."""
    assert isinstance(house_scraper, HouseDisclosureScraper)
    assert hasattr(house_scraper, 'driver')
    assert hasattr(house_scraper, 'wait')

@pytest.mark.scraper
@pytest.mark.integration
def test_senate_search_functionality(senate_scraper):
    """Test Senate disclosure search functionality."""
    # Test basic search
    results = senate_scraper.search_member_disclosures(
        last_name="Warren",
        first_name="Elizabeth",
        filing_year="2023"
    )
    assert isinstance(results, list)
    assert all(isinstance(r, dict) for r in results)
    
    # Test search with specific report types
    ptr_results = senate_scraper.search_member_disclosures(
        last_name="Tuberville",
        first_name="Thomas",
        filing_year="2023",
        report_types=['ptr']
    )
    assert all('ptr' in r['report_type'].lower() or 'transaction' in r['report_type'].lower() 
               for r in ptr_results)
    
    annual_results = senate_scraper.search_member_disclosures(
        last_name="Sanders",
        first_name="Bernard",
        filing_year="2023",
        report_types=['annual']
    )
    assert all('annual' in r['report_type'].lower() for r in annual_results)

@pytest.mark.scraper
@pytest.mark.integration
def test_house_search_functionality(house_scraper):
    """Test House disclosure search functionality."""
    # Test basic search
    results = house_scraper.search_member_disclosures(
        last_name="Pelosi",
        state="CA",
        district="11",
        filing_year="2023"
    )
    assert isinstance(results, list)
    assert all(isinstance(r, dict) for r in results)
    
    # Test search with specific report types
    ptr_results = house_scraper.search_member_disclosures(
        last_name="Pelosi",
        state="CA",
        district="11",
        filing_year="2023",
        report_types=['ptr']
    )
    assert all('ptr' in r['report_type'].lower() or 'transaction' in r['report_type'].lower() 
               for r in ptr_results)

@pytest.mark.scraper
def test_senate_session_management(senate_scraper):
    """Test Senate scraper session management."""
    # Test session recovery
    senate_scraper.with_session(force_new=True)
    assert hasattr(senate_scraper, 'driver')
    
    # Test multiple searches in same session
    results1 = senate_scraper.search_member_disclosures(
        last_name="Warren",
        first_name="Elizabeth",
        filing_year="2023"
    )
    results2 = senate_scraper.search_member_disclosures(
        last_name="Sanders",
        first_name="Bernard",
        filing_year="2023"
    )
    assert isinstance(results1, list)
    assert isinstance(results2, list)

@pytest.mark.scraper
def test_house_session_management(house_scraper):
    """Test House scraper session management."""
    # Test session recovery
    house_scraper.with_session(force_new=True)
    assert hasattr(house_scraper, 'driver')
    
    # Test multiple searches in same session
    results1 = house_scraper.search_member_disclosures(
        last_name="Pelosi",
        state="CA",
        district="11",
        filing_year="2023"
    )
    results2 = house_scraper.search_member_disclosures(
        last_name="Ocasio-Cortez",
        state="NY",
        district="14",
        filing_year="2023"
    )
    assert isinstance(results1, list)
    assert isinstance(results2, list)

@pytest.mark.scraper
def test_senate_error_handling(senate_scraper):
    """Test Senate scraper error handling."""
    # Test invalid search parameters
    with pytest.raises(Exception):
        senate_scraper.search_member_disclosures(
            last_name="",
            first_name="",
            filing_year="2023"
        )
    
    # Test invalid year
    with pytest.raises(Exception):
        senate_scraper.search_member_disclosures(
            last_name="Warren",
            first_name="Elizabeth",
            filing_year="invalid"
        )

@pytest.mark.scraper
def test_house_error_handling(house_scraper):
    """Test House scraper error handling."""
    # Test invalid search parameters
    with pytest.raises(Exception):
        house_scraper.search_member_disclosures(
            last_name="",
            state="",
            district="",
            filing_year="2023"
        )
    
    # Test invalid district
    with pytest.raises(Exception):
        house_scraper.search_member_disclosures(
            last_name="Pelosi",
            state="CA",
            district="999",
            filing_year="2023"
        ) 