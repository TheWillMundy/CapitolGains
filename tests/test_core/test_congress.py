"""Tests for core Congress class functionality."""
import pytest
import requests
import logging
from capitolgains.core.congress import Congress, CongressMember

@pytest.mark.core
def test_congress_initialization(api_key):
    """Test basic Congress class initialization."""
    congress = Congress(api_key=api_key)
    assert hasattr(congress, 'api_key')
    assert hasattr(congress, 'session')
    assert isinstance(congress.session, requests.Session)
    assert congress.session.headers.get('x-api-key') == api_key

@pytest.mark.core
def test_congress_member_initialization():
    """Test CongressMember initialization."""
    test_data = {
        'bioguideId': 'W000817',
        'name': 'Elizabeth Warren',
        'partyName': 'Democrat',
        'state': 'MA',
        'district': None,
        'url': 'https://www.congress.gov/member/elizabeth-warren/W000817',
        'terms': {
            'item': [
                {'chamber': 'Senate', 'start': '2013-01-03', 'end': '2019-01-03'},
                {'chamber': 'Senate', 'start': '2019-01-03', 'end': '2025-01-03'}
            ]
        }
    }
    
    member = CongressMember(test_data)
    assert member.bioguide_id == 'W000817'
    assert member.name == 'Elizabeth Warren'
    assert member.party == 'Democrat'
    assert member.state == 'MA'
    assert member.chamber == 'Senate'
    assert str(member) == 'Elizabeth Warren (Democrat-MA)'

@pytest.mark.core
@pytest.mark.integration
def test_get_current_congress(api_key):
    """Test getting current congress number."""
    congress = Congress(api_key=api_key)
    current_congress = congress.get_current_congress()
    assert isinstance(current_congress, int)
    assert 116 <= current_congress <= 119  # Reasonable range for current years

@pytest.mark.core
@pytest.mark.integration
def test_get_all_members(api_key):
    """Test retrieving all members of Congress."""
    congress = Congress(api_key=api_key)
    members = congress.get_all_members(118)  # Test with 118th Congress
    
    assert isinstance(members, list)
    assert len(members) > 0
    assert all(isinstance(m, CongressMember) for m in members)
    
    # Test some basic member properties
    for member in members:
        assert member.name is not None
        assert member.state is not None
        assert member.chamber in ['House', 'Senate', None]

@pytest.mark.core
def test_make_request_error_handling(api_key, caplog):
    """Test error handling in API requests."""
    caplog.set_level(logging.ERROR)
    congress = Congress(api_key=api_key)
    
    # Test with invalid endpoint (404 error)
    with caplog.at_level(logging.ERROR):
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            congress._make_request('invalid/endpoint')
        assert exc_info.value.response.status_code == 404
        assert "Not Found" in str(exc_info.value)
        assert any("API request failed: 404" in record.message for record in caplog.records)
    
    caplog.clear()
    
    # Test with invalid API key (403 error)
    with caplog.at_level(logging.ERROR):
        invalid_congress = Congress(api_key='invalid_key')
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            invalid_congress._make_request('congress')
        assert exc_info.value.response.status_code == 403
        assert "Forbidden" in str(exc_info.value)
        assert any("API request failed: 403" in record.message for record in caplog.records)
    
    caplog.clear()
    
    # Test with connection error
    with caplog.at_level(logging.ERROR):
        congress.BASE_URL = "https://invalid.example.com"
        with pytest.raises(requests.exceptions.ConnectionError):
            congress._make_request('congress')
        assert any("API request failed" in record.message for record in caplog.records)

@pytest.mark.core
def test_get_current_congress_fallback(api_key, caplog):
    """Test fallback behavior when getting current congress fails."""
    caplog.set_level(logging.ERROR)
    
    with caplog.at_level(logging.ERROR):
        congress = Congress(api_key='invalid_key')
        current_congress = congress.get_current_congress()
        assert current_congress == 118
        assert any("API request failed" in record.message for record in caplog.records) 