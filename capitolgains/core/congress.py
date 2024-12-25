"""
Congress member database functionality.

This module provides functionality to retrieve congressional member data.
"""

import logging
from typing import Dict, List, Optional
import requests

logger = logging.getLogger(__name__)

class CongressMember:
    """Represents a member of Congress with their associated information."""
    
    def __init__(self, data: Dict):
        """Initialize a CongressMember from API response data."""
        self.bioguide_id = data.get('bioguideId')
        self.name = data.get('name')
        self.party = data.get('partyName')
        self.state = data.get('state')
        self.district = data.get('district')
        self.url = data.get('url')
        self.terms = data.get('terms', {}).get('item', [])
        
        # Get current chamber from most recent term
        self.chamber = None
        if self.terms:
            latest_term = self.terms[-1]
            self.chamber = latest_term.get('chamber')
            if self.chamber == 'House of Representatives':
                self.chamber = 'House'

    def __str__(self) -> str:
        """Return string representation of the member."""
        return f"{self.name} ({self.party}-{self.state})"

class Congress:
    """Main class for retrieving congressional member data."""

    BASE_URL = "https://api.congress.gov/v3"
    
    def __init__(self, api_key: str):
        """Initialize Congress instance with API key."""
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'x-api-key': api_key,
            'accept': 'application/json'
        })

    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """Make an API request to Congress.gov."""
        url = f"{self.BASE_URL}/{endpoint}"
        params = params or {}
        params['format'] = 'json'
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise

    def get_current_congress(self) -> int:
        """Get the current congress number."""
        try:
            response = self._make_request('congress')
            if 'congress' in response:
                return int(response['congress']['number'])
            return 118  # Fallback to 118th Congress
        except Exception:
            return 118  # Fallback to 118th Congress if request fails

    def get_all_members(self, congress: Optional[int] = None) -> List[CongressMember]:
        """Get all members of Congress for a specific congress number."""
        if congress is None:
            congress = self.get_current_congress()
        
        all_members = []
        offset = 0
        limit = 250  # Maximum allowed by API
        
        while True:
            params = {
                'offset': offset,
                'limit': limit
            }
            
            data = self._make_request(f'member/congress/{congress}', params)
            
            if 'members' in data:
                members = [CongressMember(m) for m in data['members']]
                all_members.extend(members)
            
            # Check for next page
            pagination = data.get('pagination', {})
            if not pagination.get('next'):
                break
                
            offset += limit
        
        return all_members 