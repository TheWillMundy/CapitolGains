"""Tests for congress.py module."""

import os
import pytest
from capitolgains.core.congress import Congress, CongressMember

@pytest.fixture(scope="module")
def congress():
    """Create a Congress instance with API key from environment."""
    api_key = os.getenv("CONGRESS_API_KEY")
    if not api_key:
        pytest.skip("CONGRESS_API_KEY environment variable not set")
    return Congress(api_key)

@pytest.fixture(scope="module")
def current_members(congress):
    """Get current members of Congress."""
    return congress.get_all_members()

def test_congress_initialization(congress):
    """Test Congress class initialization."""
    assert congress.api_key == os.getenv("CONGRESS_API_KEY")
    assert congress.BASE_URL == "https://api.congress.gov/v3"
    assert 'x-api-key' in congress.session.headers
    assert congress.session.headers['accept'] == 'application/json'

def test_get_current_congress(congress):
    """Test getting current congress number."""
    congress_number = congress.get_current_congress()
    assert isinstance(congress_number, int)
    assert congress_number >= 118  # Will always be at least the 118th Congress

def test_get_all_members_structure(current_members):
    """Test the structure of get_all_members response."""
    assert len(current_members) > 0
    assert all(isinstance(m, CongressMember) for m in current_members)

    # Test first member's structure
    member = current_members[0]
    
    # Required fields
    assert hasattr(member, 'bioguide_id') and isinstance(member.bioguide_id, str)
    assert hasattr(member, 'name') and isinstance(member.name, str)
    assert hasattr(member, 'party') and isinstance(member.party, str)
    assert hasattr(member, 'state') and isinstance(member.state, str)
    assert hasattr(member, 'district') and (member.district is None or isinstance(member.district, int))
    assert hasattr(member, 'url') and isinstance(member.url, str)
    assert hasattr(member, 'terms') and isinstance(member.terms, list)
    assert hasattr(member, 'chamber') and member.chamber in ['House', 'Senate']

def test_member_terms_structure(current_members):
    """Test the structure of member terms."""
    for member in current_members:
        assert member.terms
        for term in member.terms:
            assert 'chamber' in term
            assert term['chamber'] in ['House of Representatives', 'Senate']
            assert 'startYear' in term
            assert isinstance(int(term['startYear']), int)
            if 'endYear' in term:  # Some current terms might not have end year
                assert isinstance(int(term['endYear']), int)

def test_congress_size(current_members):
    """Test that we have a reasonable number of Congress members."""
    assert len(current_members) >= 400  # There should always be at least this many members
    
    house_members = [m for m in current_members if m.chamber == 'House']
    senate_members = [m for m in current_members if m.chamber == 'Senate']
    
    assert len(house_members) >= 400  # House should have at least 400
    assert len(senate_members) >= 80   # Senate should have at least 80

def test_member_string_representation(current_members):
    """Test string representation of members."""
    member = current_members[0]
    str_rep = str(member)
    assert member.name in str_rep
    assert member.party in str_rep
    assert member.state in str_rep