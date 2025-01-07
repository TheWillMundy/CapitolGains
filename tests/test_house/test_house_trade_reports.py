"""Tests for House trade report functionality."""
import pytest
import pprint
from pathlib import Path
from capitolgains.core.representative import Representative

@pytest.mark.house
@pytest.mark.integration
def test_house_trade_report_basic(house_scraper, output_dir):
    """Test basic trade report retrieval for a single representative."""
    # Using Pelosi as she's known to have many trades
    rep = Representative("Pelosi", state="CA", district="11")
    disclosures = rep.get_disclosures(house_scraper, "2023")
    
    print("\nActual disclosure structure:")
    pprint.pprint(disclosures['trades'][0] if disclosures['trades'] else None)
    
    assert 'trades' in disclosures
    assert isinstance(disclosures['trades'], list)
    
    if disclosures['trades']:
        report = disclosures['trades'][0]
        assert 'filing_type' in report
        assert 'name' in report
        assert 'pdf_url' in report
        
        # Download and verify PDF
        pdf_path = house_scraper.download_disclosure_pdf(
            report['pdf_url'],
            download_dir=str(output_dir)
        )
        assert Path(pdf_path).exists()
        assert Path(pdf_path).stat().st_size > 0

@pytest.mark.house
def test_house_input_validation():
    """Test input validation for Representative class."""
    # Test invalid state
    with pytest.raises(ValueError) as exc_info:
        Representative("Test", state="XX")
    assert "Invalid state code" in str(exc_info.value)
    
    # Test valid state
    rep = Representative("Test", state="CA")  # Should not raise
    
    # Test future year
    with pytest.raises(ValueError) as exc_info:
        Representative.validate_year("2025")  # Use class method directly
    assert "Year cannot be in the future" in str(exc_info.value)
    
    # Test invalid year format
    with pytest.raises(ValueError) as exc_info:
        Representative.validate_year("invalid")  # Use class method directly
    assert "Invalid year format" in str(exc_info.value)
    
    # Test year too old
    with pytest.raises(ValueError) as exc_info:
        Representative.validate_year("1994")  # Use class method directly
    assert "Year must be 1995 or later" in str(exc_info.value)

@pytest.mark.house
@pytest.mark.integration
def test_house_trade_report_error_handling(house_scraper):
    """Test error handling for invalid trade report requests."""
    rep = Representative("Pelosi", state="CA", district="11")
    
    # Test with invalid year format (should fail before making request)
    with pytest.raises(ValueError) as exc_info:
        rep.get_disclosures(house_scraper, "invalid_year")
    assert "Invalid year format" in str(exc_info.value)
    
    # Test with future year (should fail before making request)
    with pytest.raises(ValueError) as exc_info:
        rep.get_disclosures(house_scraper, "2025")
    assert "Year cannot be in the future" in str(exc_info.value)
    
    # Test with invalid state (should fail at initialization)
    with pytest.raises(ValueError) as exc_info:
        Representative("Test", state="XX")
    assert "Invalid state code" in str(exc_info.value)
    
    # Test with invalid district (should make request but return empty results)
    invalid_rep = Representative("Pelosi", state="CA", district="999")
    result = invalid_rep.get_disclosures(house_scraper, "2023")
    assert len(result['trades']) == 0
    assert len(result['annual']) == 0

@pytest.mark.house
@pytest.mark.integration
def test_house_multiple_representatives_trades(house_scraper, test_representatives, output_dir):
    """Test trade report retrieval for multiple representatives."""
    for last_name, state, district in test_representatives:
        rep = Representative(last_name, state=state, district=district)
        disclosures = rep.get_disclosures(house_scraper, "2023")
        
        assert 'trades' in disclosures
        assert isinstance(disclosures['trades'], list)
        
        # Basic validation of report structure
        for report in disclosures['trades'][:1]:  # Test first trade only
            assert 'filing_type' in report
            assert 'name' in report
            assert 'pdf_url' in report
            
            if report['pdf_url']:
                # Verify PDF download
                pdf_path = house_scraper.download_disclosure_pdf(
                    report['pdf_url'],
                    download_dir=str(output_dir)
                )
                assert Path(pdf_path).exists()
                assert Path(pdf_path).stat().st_size > 0

@pytest.mark.house
@pytest.mark.integration
def test_house_trade_report_date_filtering(house_scraper):
    """Test trade report filtering by date."""
    rep = Representative("Pelosi", state="CA", district="11")
    
    # Test different years
    years = ["2022", "2023"]
    previous_count = None
    
    for year in years:
        disclosures = rep.get_disclosures(house_scraper, year)
        current_count = len(disclosures['trades'])
        
        # Ensure we get different results for different years
        if previous_count is not None:
            assert current_count != previous_count, f"Expected different number of trades for {year}"
        
        previous_count = current_count

@pytest.mark.house
@pytest.mark.integration
def test_house_pdf_download_error_handling(house_scraper, output_dir):
    """Test error handling for PDF downloads."""
    # Test with invalid URL
    with pytest.raises(Exception):
        house_scraper.download_disclosure_pdf(
            "https://invalid-url/file.pdf",
            download_dir=str(output_dir)
        )
    
    # Test with non-PDF URL
    with pytest.raises(Exception):
        house_scraper.download_disclosure_pdf(
            "https://www.house.gov",
            download_dir=str(output_dir)
        ) 