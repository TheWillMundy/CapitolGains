"""Tests for scraper utility functions."""
import pytest
from pathlib import Path
from capitolgains.utils.senator_scraper import SenateDisclosureScraper
from capitolgains.utils.representative_scraper import HouseDisclosureScraper, ReportType

@pytest.mark.scraper
def test_senate_scraper_initialization(senate_scraper):
    """Test Senate scraper initialization."""
    assert isinstance(senate_scraper, SenateDisclosureScraper)
    assert hasattr(senate_scraper, '_browser')
    assert hasattr(senate_scraper, '_page')
    assert hasattr(senate_scraper, '_context')

@pytest.mark.scraper
def test_house_scraper_initialization(house_scraper):
    """Test House scraper initialization."""
    assert isinstance(house_scraper, HouseDisclosureScraper)
    assert hasattr(house_scraper, '_browser')
    assert hasattr(house_scraper, '_page')
    assert hasattr(house_scraper, '_context')

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
    assert all('ptr' in r['filing_type'].lower() or 'transaction' in r['filing_type'].lower() 
               for r in ptr_results)

@pytest.mark.scraper
def test_senate_session_management(senate_scraper):
    """Test Senate scraper session management."""
    # Test session recovery
    senate_scraper.with_session(force_new=True)
    assert hasattr(senate_scraper, '_browser')
    assert hasattr(senate_scraper, '_page')
    
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
    assert hasattr(house_scraper, '_browser')
    assert hasattr(house_scraper, '_page')
    
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
def test_senate_error_handling(senate_scraper, future_year):
    """Test Senate scraper error handling for year validation."""
    # Test invalid year format
    with pytest.raises(ValueError, match="Invalid year format"):
        senate_scraper.search_member_disclosures(
            last_name="Warren",
            first_name="Elizabeth",
            filing_year="invalid"
        )
    
    # Test future year
    with pytest.raises(ValueError, match="Year cannot be in the future"):
        senate_scraper.search_member_disclosures(
            last_name="Warren",
            first_name="Elizabeth",
            filing_year=future_year
        )
    
    # Test year too old
    with pytest.raises(ValueError, match="Year must be 2012 or later"):
        senate_scraper.search_member_disclosures(
            last_name="Warren",
            first_name="Elizabeth",
            filing_year="2011"
        )

@pytest.mark.scraper
def test_house_error_handling(house_scraper, future_year):
    """Test House scraper error handling for year validation."""
    # Test invalid year format
    with pytest.raises(ValueError, match="Invalid year format"):
        house_scraper.search_member_disclosures(
            last_name="Pelosi",
            state="CA",
            district="11",
            filing_year="invalid"
        )
    
    # Test future year
    with pytest.raises(ValueError, match="Year cannot be in the future"):
        house_scraper.search_member_disclosures(
            last_name="Pelosi",
            state="CA",
            district="11",
            filing_year=future_year
        )
    
    # Test year too old
    with pytest.raises(ValueError, match="Year must be 1995 or later"):
        house_scraper.search_member_disclosures(
            last_name="Pelosi",
            state="CA",
            district="11",
            filing_year="1994"
        )

@pytest.mark.scraper
def test_report_type_validation():
    """Test report type validation for both House and Senate scrapers."""
    # Test with House scraper
    with HouseDisclosureScraper() as house_scraper:
        # Test invalid report type string
        with pytest.raises(ValueError, match="Invalid report type"):
            house_scraper.search_member_disclosures(
                last_name="Pelosi",
                state="CA",
                district="11",
                filing_year="2023",
                report_types=['invalid_type']
            )
        
        # Test invalid report type object
        with pytest.raises(ValueError, match="Invalid report type"):
            house_scraper.search_member_disclosures(
                last_name="Pelosi",
                state="CA",
                district="11",
                filing_year="2023",
                report_types=[123]  # Non-string, non-Enum type
            )
        
        # Test valid report type enum
        results = house_scraper.search_member_disclosures(
            last_name="Pelosi",
            state="CA",
            district="11",
            filing_year="2023",
            report_types=[ReportType.PTR]  # Using Enum directly
        )
        assert isinstance(results, list)
    
    # Test with Senate scraper
    with SenateDisclosureScraper() as senate_scraper:
        # Test valid report type enum
        results = senate_scraper.search_member_disclosures(
            last_name="Warren",
            first_name="Elizabeth",
            filing_year="2023",
            report_types=[ReportType.PTR]  # Using Enum directly
        )
        assert isinstance(results, list) 