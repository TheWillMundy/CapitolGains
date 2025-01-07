"""Tests for Senate annual report functionality."""
import pytest
from capitolgains.core.senator import Senator

@pytest.mark.senate
@pytest.mark.integration
def test_annual_report_basic(senate_scraper, output_dir):
    """Test basic annual report retrieval for a single senator."""
    senator = Senator("Warren", first_name="Elizabeth", state="MA")
    disclosures = senator.get_disclosures(senate_scraper, "2023")
    
    assert 'annual' in disclosures
    assert isinstance(disclosures['annual'], list)
    
    if disclosures['annual']:
        report = disclosures['annual'][0]
        assert 'report_type' in report
        assert 'date' in report
        assert 'report_url' in report
        
        # Process the report
        result = senate_scraper.process_filing(
            report['report_url'],
            report_type='annual',
            download_dir=str(output_dir)
        )
        
        assert result['type'] in ['web_table', 'pdf']
        if result['type'] == 'web_table':
            assert 'metadata' in result
            assert 'sections' in result
            
            for section in result['sections']:
                assert 'title' in section
                if section['title'] != 'Attachments & Comments':
                    if section['table']:
                        assert 'headers' in section['table']
                        assert 'rows' in section['table']

@pytest.mark.senate
@pytest.mark.integration
def test_annual_report_amendments(senate_scraper, output_dir):
    """Test processing of annual report amendments."""
    senator = Senator("Blackburn", first_name="Marsha", state="TN")
    disclosures = senate_scraper.search_member_disclosures(
        last_name="Blackburn",
        first_name="Marsha",
        filing_year="2019",
        report_types=['annual']
    )
    
    amendments = [d for d in disclosures if 'amendment' in d['report_type'].lower()]
    assert len(amendments) > 0, "Expected at least one amendment"
    
    for amendment in amendments[:1]:  # Test first amendment
        result = senate_scraper.process_filing(
            amendment['report_url'],
            report_type='amendment',
            download_dir=str(output_dir)
        )
        
        assert result['type'] in ['web_table', 'pdf']
        if result['type'] == 'web_table':
            assert 'metadata' in result
            assert 'sections' in result

@pytest.mark.senate
@pytest.mark.integration
def test_multiple_senators_annual(senate_scraper, test_senators):
    """Test annual report retrieval for multiple senators."""
    for last_name, first_name, state in test_senators:
        senator = Senator(last_name, first_name=first_name, state=state)
        disclosures = senator.get_disclosures(senate_scraper, "2023")
        
        assert 'annual' in disclosures
        assert isinstance(disclosures['annual'], list)
        
        # Basic validation of report structure
        for report in disclosures['annual']:
            assert 'report_type' in report
            assert 'date' in report
            assert 'report_url' in report

@pytest.mark.senate
@pytest.mark.integration
def test_annual_report_error_handling(senate_scraper):
    """Test error handling for invalid senator data."""
    invalid_senator = Senator("NonexistentSenator", first_name="Invalid", state="XX")
    
    with pytest.raises(ValueError) as exc_info:  # Changed to ValueError to match our validation
        invalid_senator.get_disclosures(senate_scraper, "2023")
    assert "Invalid state code for Senate" in str(exc_info.value) 