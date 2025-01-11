"""House Representative financial disclosure functionality.

This module provides functionality to retrieve and process financial disclosures for
House Representatives. It handles:
- Searching and retrieving financial disclosures
- Caching disclosure data to minimize network requests
- Filtering and categorizing disclosures by type
- Downloading disclosure PDFs

The House disclosure system has specific requirements and limitations:
- Electronic records are available from 1995 onwards
- Disclosures are categorized into trades (PTRs) and annual reports (FDs)
- All disclosures are provided as PDFs
"""

from datetime import datetime
from typing import List, Dict, Any, Optional, ClassVar, Set
from capitolgains.utils.representative_scraper import HouseDisclosureScraper
import logging

logger = logging.getLogger(__name__)

class Representative:
    """A House Representative and their financial disclosures.
    
    This class provides functionality to:
    - Search and retrieve financial disclosures
    - Cache disclosure data to minimize network requests
    - Filter and categorize disclosures by type
    - Download disclosure PDFs
    
    Attributes:
        name: Representative's last name used for searches
        state: Two-letter state code (optional)
        district: District number (optional)
        _cached_disclosures: Internal cache mapping years to disclosure data
        VALID_STATES: Set of valid two-letter state/territory codes
    """
    
    VALID_STATES: ClassVar[Set[str]] = {
        'AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE',
        'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
        'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE',
        'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK',
        'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT',
        'VI', 'VA', 'WA', 'WV', 'WI', 'WY'
    }

    @staticmethod
    def validate_year(year: str) -> None:
        """Validate that a year is valid for searching.
        
        Args:
            year: Year string to validate
            
        Raises:
            ValueError: If the year is invalid or in an invalid format
            
        Note:
            - Years must be 1995 or later (when electronic records began)
            - Only strictly future years are invalid
        """
        try:
            year_int = int(year)
            current_year = datetime.now().year
            
            if year_int < 1995:  # House electronic records start from 1995
                raise ValueError(f"Year must be 1995 or later, got {year}")
            if year_int > current_year:  # Only block strictly future years
                raise ValueError(f"Year cannot be in the future (current year is {current_year}), got {year}")
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                raise ValueError(f"Invalid year format: {year}. Must be a valid year number.")
            raise

    @classmethod
    def validate_state(cls, state: Optional[str]) -> None:
        """Validate that a state code is valid.
        
        Args:
            state: Two-letter state code to validate, or None
            
        Raises:
            ValueError: If the state code is invalid
            
        Note:
            Valid codes include all US states, territories, and DC
        """
        if state is not None and state not in cls.VALID_STATES:
            valid_states = ', '.join(sorted(cls.VALID_STATES))
            raise ValueError(
                f"Invalid state code: {state}. Must be one of: {valid_states}"
            )

    @classmethod
    def get_member_disclosures(
        cls,
        name: str,
        year: Optional[str] = None,
        state: Optional[str] = None,
        district: Optional[str] = None,
        headless: bool = True
    ) -> Dict[str, List[Dict[str, Any]]]:
        """Get financial disclosures for a single representative.
        
        This method handles the scraper lifecycle management for simple single-member
        queries. For bulk processing, use the scraper directly with context management.
        
        Args:
            name: Representative's last name
            year: Year to search for (defaults to current year)
            state: Two-letter state code (optional)
            district: District number (optional)
            headless: Whether to run browser in headless mode
            
        Returns:
            Dictionary with categorized disclosures:
            {
                'trades': List of PTR disclosures,
                'annual': List of annual disclosures (FD),
                'amendments': List of amendments,
                'blind_trust': List of blind trust disclosures,
                'extension': List of extension requests,
                'new_filer': List of new filer reports,
                'termination': List of termination reports,
                'other': List of other disclosures
            }
            
        Example:
            ```python
            # Simple single-member usage
            disclosures = Representative.get_member_disclosures(
                "Pelosi", state="CA", district="11", year="2023"
            )
            ```
        """
        # Validate inputs before creating scraper
        if year is None:
            year = str(datetime.now().year)
        cls.validate_year(year)
        cls.validate_state(state)
        
        with HouseDisclosureScraper(headless=headless) as scraper:
            rep = cls(name, state=state, district=district)
            return rep.get_disclosures(scraper, year=year)
    
    def __init__(self, name: str, state: Optional[str] = None, district: Optional[str] = None):
        """Initialize a Representative instance.
        
        Args:
            name: Representative's last name
            state: Two-letter state code (optional)
            district: District number (optional)
            
        Note:
            While state and district are optional, providing them improves accuracy
            by ensuring only disclosures from the correct representative are returned.
        """
        self.name = name
        self.validate_state(state)  # Validate state on initialization
        self.state = state
        self.district = district
        self._cached_disclosures: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
        
    def get_disclosures(self, scraper: HouseDisclosureScraper, year: Optional[str] = None) -> Dict[str, List[Dict[str, Any]]]:
        """Get all disclosures for the representative for a given year.
        
        This method fetches both Periodic Transaction Reports (PTRs) and Annual Financial
        Disclosures (FDs) for the specified year. Results are cached to minimize network requests.
        
        Args:
            scraper: Instance of HouseDisclosureScraper to use for fetching data
            year: Year to search for (defaults to current year)
            
        Returns:
            Dictionary with categorized disclosures:
            {
                'trades': List of PTR disclosures,
                'annual': List of annual disclosures (FD),
                'amendments': List of amendments,
                'blind_trust': List of blind trust disclosures,
                'extension': List of extension requests,
                'new_filer': List of new filer reports,
                'termination': List of termination reports,
                'other': List of other disclosures
            }
            
        Note:
            Results are filtered to ensure they match the representative's state and district
            if those were provided during initialization.
        """
        if not year:
            year = str(datetime.now().year)
            
        # Check cache first for efficiency
        if year in self._cached_disclosures:
            return self._cached_disclosures[year]
            
        # Perform single search for all disclosures
        all_disclosures = scraper.search_member_disclosures(
            last_name=self.name,
            filing_year=year,
            state=self.state,
            district=self.district
        )
        
        # Filter results to ensure they match our representative
        filtered_disclosures = [
            d for d in all_disclosures 
            if self._matches_representative(d)
        ]
        
        # Categorize disclosures by type
        categorized = {
            'trades': [d for d in filtered_disclosures if 'ptr' in d['filing_type'].lower() or 'transaction' in d['filing_type'].lower()],
            'annual': [d for d in filtered_disclosures if 'fd' in d['filing_type'].lower() and not 'amendment' in d['filing_type'].lower()],
            'amendments': [d for d in filtered_disclosures if 'amendment' in d['filing_type'].lower()],
            'blind_trust': [d for d in filtered_disclosures if 'blind trust' in d['filing_type'].lower()],
            'extension': [d for d in filtered_disclosures if 'extension' in d['filing_type'].lower()],
            'new_filer': [d for d in filtered_disclosures if 'new filer' in d['filing_type'].lower()],
            'termination': [d for d in filtered_disclosures if 'termination' in d['filing_type'].lower()],
            'other': [d for d in filtered_disclosures if not any(
                x in d['filing_type'].lower() for x in 
                ['ptr', 'transaction', 'fd', 'amendment', 'blind trust', 'extension', 'new filer', 'termination']
            )]
        }
        
        # Cache the results
        self._cached_disclosures[year] = categorized
        return categorized
        
    def _matches_representative(self, disclosure: Dict[str, Any]) -> bool:
        """Check if a disclosure matches this representative's details.
        
        Args:
            disclosure: Disclosure dictionary from search results
            
        Returns:
            True if the disclosure matches this representative's details
            
        Note:
            Matches are performed using:
            1. Office field (state-district) if available
            2. Name matching as fallback
        """
        office = disclosure.get('office', '')
        
        # If we have state/district and office is present, use that for matching
        if office and (self.state or self.district):
            # Try hyphenated format first (e.g., "CA-11")
            office_parts = office.split('-')
            if len(office_parts) == 2:
                disc_state = office_parts[0].strip()
                disc_district = office_parts[1].strip()
            else:
                # Try non-hyphenated format (e.g., "CA11")
                if len(office) >= 3:  # Need at least "XX1"
                    disc_state = office[:2].strip()
                    disc_district = office[2:].strip()
                else:
                    return False
            
            # If state is specified and doesn't match, return False
            if self.state and disc_state != self.state:
                return False
                
            # If district is specified and doesn't match, return False
            if self.district and disc_district != self.district:
                return False
                
            # If we got here and had either state or district specified, it's a match
            return True
            
        # If we get here, either:
        # 1. We don't have state/district info to match against
        # 2. Office wasn't present in the disclosure
        # In these cases, we just verify the name matches
        name = disclosure.get('name', '').lower()
        if not name:
            return False
            
        # Simple case-insensitive check if the last name appears in the full name
        return self.name.lower() in name
        
    def get_recent_trades(self, scraper: HouseDisclosureScraper, year: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get recent trades (PTRs) for the representative.
        
        Args:
            scraper: Instance of HouseDisclosureScraper to use
            year: Year to search for trades (defaults to current year)
            
        Returns:
            List of trade dictionaries, each containing filing details and PDF URL
        """
        disclosures = self.get_disclosures(scraper, year)
        return disclosures['trades']
        
    def get_annual_disclosure(self, scraper: HouseDisclosureScraper, year: int) -> Dict[str, Any]:
        """Get annual financial disclosure for the representative.
        
        This method retrieves the annual Financial Disclosure (FD) report for the specified
        year. If multiple reports exist (e.g., amendments), it returns the original filing.
        
        Args:
            scraper: Instance of HouseDisclosureScraper to use
            year: Year to get disclosure for
            
        Returns:
            Dictionary containing disclosure information and local file path
            
        Raises:
            ValueError: If no annual disclosure is found for the specified year
        """
        disclosures = self.get_disclosures(scraper, str(year))
        annual_reports = disclosures['annual']
        
        if not annual_reports:
            raise ValueError(f"No annual disclosure found for {self.name} in {year}")
            
        # Sort by filing type to prioritize original filings over amendments
        annual_reports.sort(key=lambda x: x['filing_type'])
        disclosure = annual_reports[0]
        
        # Download the PDF if URL exists
        if disclosure['pdf_url']:
            file_path = scraper.download_disclosure_pdf(disclosure['pdf_url'])
            disclosure['file_path'] = file_path
            
        return disclosure 