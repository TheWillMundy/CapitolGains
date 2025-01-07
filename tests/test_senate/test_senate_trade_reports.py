"""Tests for Senate trade report functionality."""
import pytest
from capitolgains.core.senator import Senator
import logging

@pytest.mark.senate
@pytest.mark.integration
def test_senate_trade_report_basic(senate_scraper, output_dir):
    """Test basic trade report retrieval for a single senator."""
    # Using Tuberville as he's known to have many trades
    senator = Senator("Tuberville", first_name="Thomas", state="AL")
    disclosures = senator.get_disclosures(senate_scraper, "2023")
    
    assert 'trades' in disclosures
    assert isinstance(disclosures['trades'], list)
    
    if disclosures['trades']:
        report = disclosures['trades'][0]
        assert 'report_type' in report
        assert 'date' in report
        assert 'report_url' in report
        
        # Process the report
        result = senate_scraper.process_filing(
            report['report_url'],
            report_type='ptr',
            download_dir=str(output_dir)
        )
        
        assert result['type'] in ['web_table', 'pdf']
        if result['type'] == 'web_table':
            assert 'metadata' in result
            assert 'sections' in result
            
            # Validate trade data structure
            for section in result['sections']:
                if section['table']:
                    assert 'headers' in section['table']
                    assert 'rows' in section['table']
                    
                    # Check for required trade information columns
                    headers = [h.lower() for h in section['table']['headers']]
                    assert any('asset' in h for h in headers)
                    assert any('transaction' in h for h in headers)
                    assert any('amount' in h for h in headers)

@pytest.mark.senate
@pytest.mark.integration
def test_senate_recent_trades(senate_scraper):
    """Test the get_recent_trades convenience method."""
    senator = Senator("Tuberville", first_name="Thomas", state="AL")
    trades = senator.get_recent_trades(senate_scraper, year="2023")
    
    assert isinstance(trades, list)
    if trades:
        for trade in trades:
            assert 'report_type' in trade
            assert 'date' in trade
            assert 'report_url' in trade
            assert 'ptr' in trade['report_type'].lower() or 'transaction' in trade['report_type'].lower()

@pytest.mark.senate
@pytest.mark.integration
def test_senate_multiple_senators_trades(senate_scraper, test_senators):
    """Test trade report retrieval for multiple senators."""
    for last_name, first_name, state in test_senators:
        senator = Senator(last_name, first_name=first_name, state=state)
        disclosures = senator.get_disclosures(senate_scraper, "2023")
        
        assert 'trades' in disclosures
        assert isinstance(disclosures['trades'], list)
        
        # Basic validation of report structure
        for report in disclosures['trades']:
            assert 'report_type' in report
            assert 'date' in report
            assert 'report_url' in report

@pytest.mark.senate
@pytest.mark.integration
def test_senate_trade_report_date_filtering(senate_scraper):
    """Test trade report filtering by date."""
    logging.getLogger('capitolgains').setLevel(logging.DEBUG)
    
    senator = Senator("Tuberville", first_name="Thomas", state="AL")
    
    # Test with 2022
    start_date = "01/01/2022"
    end_date = "12/31/2022"
    print(f"\nFetching 2022 trades ({start_date} to {end_date})")
    year_2022 = senator.get_disclosures(
        senate_scraper,
        start_date=start_date,
        end_date=end_date
    )
    print("\nRaw 2022 response:")
    print(year_2022)
    print(f"2022 trades: {len(year_2022['trades'])}")
    for trade in year_2022['trades']:
        print(f"  - {trade['date']}: {trade['report_type']}")
    
    # Test with 2023
    start_date = "01/01/2023"
    end_date = "12/31/2023"
    print(f"\nFetching 2023 trades ({start_date} to {end_date})")
    year_2023 = senator.get_disclosures(
        senate_scraper,
        start_date=start_date,
        end_date=end_date
    )
    print("\nRaw 2023 response:")
    print(year_2023)
    print(f"2023 trades: {len(year_2023['trades'])}")
    for trade in year_2023['trades']:
        print(f"  - {trade['date']}: {trade['report_type']}")
    
    # Get report titles and dates for comparison
    year_2022_reports = {(r['report_type'], r['date']) for r in year_2022['trades']}
    year_2023_reports = {(r['report_type'], r['date']) for r in year_2023['trades']}
    
    print(f"\n2022 unique reports: {year_2022_reports}")
    print(f"2023 unique reports: {year_2023_reports}")
    
    # Verify reports are unique between years
    assert year_2022_reports != year_2023_reports, \
        "Expected different reports for different years"
    
    # Verify dates fall within specified ranges
    for report in year_2022['trades']:
        report_date = report['date']
        assert report_date >= "01/01/2022" and report_date <= "12/31/2022", \
            f"Report date {report_date} outside 2022 range"
    
    for report in year_2023['trades']:
        report_date = report['date']
        assert report_date >= "01/01/2023" and report_date <= "12/31/2023", \
            f"Report date {report_date} outside 2023 range"
    
    # Test with just start date
    start_only = senator.get_disclosures(
        senate_scraper,
        start_date="01/01/2022"
    )
    assert isinstance(start_only['trades'], list)
    for report in start_only['trades']:
        assert report['date'] >= "01/01/2022", \
            f"Report date {report['date']} before start date"
    
    # Test with just end date
    end_only = senator.get_disclosures(
        senate_scraper,
        end_date="12/31/2023"
    )
    assert isinstance(end_only['trades'], list)
    for report in end_only['trades']:
        assert report['date'] <= "12/31/2023", \
            f"Report date {report['date']} after end date"
    
    # Test with year parameter
    year_results = senator.get_disclosures(senate_scraper, year="2022")
    assert isinstance(year_results['trades'], list)
    for report in year_results['trades']:
        assert "2022" in report['date'], \
            f"Report date {report['date']} not in specified year"

@pytest.mark.senate
@pytest.mark.integration
def test_senate_trade_report_error_handling(senate_scraper):
    """Test error handling for invalid trade report requests."""
    senator = Senator("Tuberville", first_name="Thomas", state="AL")
    
    # Test with invalid date format
    with pytest.raises(ValueError) as exc_info:
        senator.get_disclosures(senate_scraper, start_date="2023-01-01")
    assert "Invalid date format" in str(exc_info.value)
    
    # Test with date before 2012
    with pytest.raises(ValueError) as exc_info:
        senator.get_disclosures(senate_scraper, start_date="01/01/2011")
    assert "only available from 2012 onwards" in str(exc_info.value)
    
    # Test with invalid year format
    with pytest.raises(ValueError) as exc_info:
        senator.get_disclosures(senate_scraper, year="invalid_year")
    assert "Invalid date format" in str(exc_info.value)
    
    # Test with end date before start date
    with pytest.raises(ValueError) as exc_info:
        senator.get_disclosures(
            senate_scraper,
            start_date="12/31/2023",
            end_date="01/01/2023"
        )
    assert "End date cannot be before start date" in str(exc_info.value)

@pytest.mark.senate
def test_senate_input_validation():
    """Test input validation for Senator class."""
    # Test invalid state (territory)
    with pytest.raises(ValueError) as exc_info:
        Senator("Test", state="PR")  # Puerto Rico doesn't have senators
    assert "Invalid state code for Senate" in str(exc_info.value)
    
    # Test invalid state (DC)
    with pytest.raises(ValueError) as exc_info:
        Senator("Test", state="DC")  # DC doesn't have senators
    assert "Invalid state code for Senate" in str(exc_info.value)
    
    # Test invalid state (made up)
    with pytest.raises(ValueError) as exc_info:
        Senator("Test", state="XX")
    assert "Invalid state code for Senate" in str(exc_info.value)
    
    # Test valid state
    senator = Senator("Test", state="CA")  # Should not raise
    assert senator.state == "CA"
    
    # Test None state
    senator = Senator("Test", state=None)  # Should not raise
    assert senator.state is None 