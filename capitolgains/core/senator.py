"""Senate member functionality.

This module provides the Senator class for managing Senate member data
and their financial disclosures. It handles caching of disclosure data and provides
methods to fetch both periodic transaction reports (PTRs) and annual financial disclosures.

The Senate disclosure system has some key differences from the House system:
- Requires accepting terms before searching
- Uses a different categorization system for reports
- Includes additional report types (blind trusts, extensions)
"""

from datetime import datetime
from typing import List, Dict, Any, Optional
from capitolgains.utils.senate_scraper import SenateDisclosureScraper

class Senator:
    """Class representing a Senator and their financial disclosures.
    
    This class provides functionality to:
    - Search and retrieve financial disclosures
    - Cache disclosure data to minimize network requests
    - Filter and categorize disclosures by type
    - Download disclosure PDFs
    
    The Senate disclosure system includes more report types than the House system,
    including blind trusts and filing extensions. This class handles these additional
    categories while maintaining a similar interface to the Representative class.
    
    Attributes:
        name: Senator's last name used for searches
        first_name: Senator's first name (optional)
        state: Two-letter state code (optional)
        _cached_disclosures: Internal cache mapping years to disclosure data
    """
    
    def __init__(self, name: str, first_name: Optional[str] = None, state: Optional[str] = None):
        """Initialize a Senator instance.
        
        Args:
            name: Senator's last name
            first_name: Senator's first name (optional)
            state: Two-letter state code (optional)
            
        Note:
            While first_name and state are optional, providing them improves accuracy
            by ensuring only disclosures from the correct senator are returned.
            This is especially important for senators with common last names.
        """
        self.name = name
        self.first_name = first_name
        self.state = state
        self._cached_disclosures: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
        
    def get_disclosures(self, scraper: SenateDisclosureScraper, year: Optional[str] = None) -> Dict[str, List[Dict[str, Any]]]:
        """Get all disclosures for the senator for a given year.
        
        This method fetches all types of financial disclosures for the specified year:
        - Periodic Transaction Reports (PTRs)
        - Annual Financial Disclosures (FDs)
        - Blind Trust Reports
        - Filing Extensions
        - Other Documents
        
        Results are cached to minimize network requests.
        
        Args:
            scraper: Instance of SenateDisclosureScraper to use for fetching data
            year: Year to search for (defaults to current year)
            
        Returns:
            Dictionary with categorized disclosures:
            {
                'trades': List of PTR disclosures,
                'annual': List of annual disclosures (FD),
                'blind_trust': List of blind trust disclosures,
                'extension': List of extension requests,
                'other': List of other disclosures
            }
        """
        if not year:
            year = str(datetime.now().year)
            
        # Return cached results if available
        if year in self._cached_disclosures:
            return self._cached_disclosures[year]
            
        # Fetch all disclosure types in one request
        all_disclosures = scraper.search_member_disclosures(
            last_name=self.name,
            filing_year=year,
            first_name=self.first_name,
            state=self.state,
            report_types=['annual', 'ptr', 'extension', 'blind_trust', 'other']
        )
        
        # Filter results to ensure they match our senator
        filtered_disclosures = [
            d for d in all_disclosures 
            if self._matches_senator(d)
        ]
        
        # Initialize categories
        categorized = {
            'trades': [],
            'annual': [],
            'blind_trust': [],
            'extension': [],
            'other': []
        }
        
        # Categorize disclosures by type
        for disclosure in filtered_disclosures:
            report_type = disclosure['report_type'].lower()
            
            # Map report types to categories
            if 'periodic transaction' in report_type:
                categorized['trades'].append(disclosure)
            elif 'annual' in report_type:
                categorized['annual'].append(disclosure)
            elif 'blind trust' in report_type:
                categorized['blind_trust'].append(disclosure)
            elif 'extension' in report_type:
                categorized['extension'].append(disclosure)
            else:
                categorized['other'].append(disclosure)
        
        # Cache results
        self._cached_disclosures[year] = categorized
        return categorized
        
    def _matches_senator(self, disclosure: Dict[str, Any]) -> bool:
        """Check if a disclosure matches this senator's details.
        
        Performs case-insensitive matching on name and state (if provided).
        This is important because the Senate system sometimes returns results
        in different cases (e.g., "WARREN" vs "Warren").
        
        Args:
            disclosure: Disclosure dictionary from search results
            
        Returns:
            True if the disclosure matches this senator's details, False otherwise
        """
        # Check first name if provided
        if self.first_name and disclosure['first_name'].lower() != self.first_name.lower():
            return False
            
        # Check last name
        if disclosure['last_name'].lower() != self.name.lower():
            return False
            
        # Check state if provided
        if self.state:
            office = disclosure['office']
            if not any(part.strip() == self.state for part in office.split(',')):
                return False
                
        return True
        
    def get_recent_trades(self, scraper: SenateDisclosureScraper, year: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get recent trades (PTRs) for the senator.
        
        Args:
            scraper: Instance of SenateDisclosureScraper to use
            year: Year to search for trades (defaults to current year)
            
        Returns:
            List of trade dictionaries, each containing filing details and PDF URL
        """
        disclosures = self.get_disclosures(scraper, year)
        return disclosures['trades']
        
    def get_annual_disclosure(self, scraper: SenateDisclosureScraper, year: int) -> Dict[str, Any]:
        """Get annual financial disclosure for the senator.
        
        This method retrieves the annual Financial Disclosure (FD) report for the specified
        year. If multiple reports exist (e.g., amendments), it returns the original filing.
        
        Args:
            scraper: Instance of SenateDisclosureScraper to use
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
            
        # Sort by report type to prioritize original filings over amendments
        annual_reports.sort(key=lambda x: 'amendment' in x['report_type'].lower())
        disclosure = annual_reports[0]
        
        # Download the PDF if URL exists
        if disclosure['pdf_url']:
            file_path = scraper.download_disclosure_pdf(disclosure['pdf_url'])
            disclosure['file_path'] = file_path
            
        return disclosure 