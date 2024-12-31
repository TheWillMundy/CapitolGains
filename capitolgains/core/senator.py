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
import logging

logger = logging.getLogger(__name__)

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
        
    def get_disclosures(
        self, 
        scraper: SenateDisclosureScraper, 
        year: Optional[str] = None,
        include_candidate_reports: bool = False,
        test_mode: bool = False
    ) -> Dict[str, List[Dict[str, Any]]]:
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
            include_candidate_reports: Whether to include candidate reports (defaults to False)
            test_mode: If True, only return one match per category (for testing)
            
        Returns:
            Dictionary with categorized disclosures:
            {
                'trades': List of PTR disclosures,
                'annual': List of annual disclosures (FD),
                'amendments': List of amendments,
                'blind_trust': List of blind trust disclosures,
                'extension': List of extension requests,
                'other': List of other disclosures
            }
        """
        if not year:
            year = str(datetime.now().year)
            
        # Create a cache key that includes the candidate reports setting
        cache_key = f"{year}_{include_candidate_reports}_{test_mode}"
        if cache_key in self._cached_disclosures:
            return self._cached_disclosures[cache_key]
            
        # Fetch all disclosure types in one request
        all_disclosures = scraper.search_member_disclosures(
            last_name=self.name,
            filing_year=year,
            first_name=self.first_name,
            state=self.state,
            report_types=['annual', 'ptr', 'extension', 'blind_trust', 'other'],
            include_candidate_reports=include_candidate_reports
        )
        
        # Filter results to ensure they match our senator
        filtered_disclosures = [
            d for d in all_disclosures 
            if self._matches_senator(d)
        ]
        
        logger.info(f"Found {len(filtered_disclosures)} total disclosures for {self.name}")
        
        # Initialize categories
        categorized = {
            'trades': [],
            'annual': [],
            'amendments': [],
            'blind_trust': [],
            'extension': [],
            'other': []
        }
        
        # Categorize disclosures by type
        for disclosure in filtered_disclosures:
            report_type = disclosure['report_type'].lower()
            
            # First check for extensions and amendments as they may contain other keywords
            if 'extension' in report_type or 'due date' in report_type:
                logger.info(f"Found extension: {disclosure['report_type']}")
                if not test_mode or len(categorized['extension']) == 0:
                    categorized['extension'].append(disclosure)
                continue
                
            if 'amendment' in report_type:
                logger.info(f"Found amendment: {disclosure['report_type']}")
                if not test_mode or len(categorized['amendments']) == 0:
                    categorized['amendments'].append(disclosure)
                continue
                
            # Then check other categories
            if 'periodic transaction' in report_type:
                if not test_mode or len(categorized['trades']) == 0:
                    logger.info(f"Found PTR: {disclosure['report_type']}")
                    categorized['trades'].append(disclosure)
            elif ('annual report for cy' in report_type or
                  'financial disclosure report' in report_type or 
                  'public financial disclosure' in report_type or
                  report_type == 'annual report'):
                logger.info(f"Found annual report: {disclosure['report_type']}")
                if not test_mode or len(categorized['annual']) == 0:
                    categorized['annual'].append(disclosure)
            elif 'blind trust' in report_type:
                if not test_mode or len(categorized['blind_trust']) == 0:
                    categorized['blind_trust'].append(disclosure)
            else:
                logger.info(f"Uncategorized report type: {disclosure['report_type']}")
                if not test_mode or len(categorized['other']) == 0:
                    categorized['other'].append(disclosure)
        
        # Cache results with the combined key
        self._cached_disclosures[cache_key] = categorized
        return categorized
        
    def _matches_senator(self, disclosure: Dict[str, Any]) -> bool:
        """Check if a disclosure matches this senator's details.
        
        The Senate system returns names in various formats:
        - First name might include middle initial/name
        - Office field might not include state
        - Last name might be repeated in office field
        
        Args:
            disclosure: Disclosure dictionary from search results
            
        Returns:
            True if the disclosure matches this senator's details, False otherwise
        """
        logger.info(f"Checking match for disclosure: {disclosure['first_name']} {disclosure['last_name']}, {disclosure['office']}")
        
        # Check last name first (most reliable)
        if disclosure['last_name'].lower() != self.name.lower():
            logger.info(f"Last name mismatch: {disclosure['last_name'].lower()} vs {self.name.lower()}")
            return False
            
        # Check first name if provided - more lenient matching
        if self.first_name:
            disclosure_first = disclosure['first_name'].lower()
            our_first = self.first_name.lower()
            # Accept if either name starts with the other
            if not (disclosure_first.startswith(our_first) or our_first.startswith(disclosure_first)):
                logger.info(f"First name mismatch: {disclosure_first} vs {our_first}")
                return False
        
        # For state matching, we'll be more lenient since the office field is inconsistent
        # If we have a state requirement but can't verify it, we'll trust the other matches
        # This works because we're already filtering by name in the search
        if self.state:
            office = disclosure['office'].lower()
            state_patterns = [
                f", {self.state.lower()}",  # "Tuberville, Tommy (Senator), AL"
                f"({self.state.lower()})",  # "Tuberville (AL)"
                f" {self.state.lower()} ",  # "AL Senator"
                self.state.lower()          # Just the state somewhere
            ]
            state_found = any(pattern in office for pattern in state_patterns)
            if not state_found:
                logger.info(f"Note: State {self.state} not found in office field: {office} - trusting name match")
        
        logger.info("Disclosure matches senator")
        return True
        
    def get_recent_trades(self, scraper: SenateDisclosureScraper, year: Optional[str] = None, test_mode: bool = False) -> List[Dict[str, Any]]:
        """Get recent trades (PTRs) for the senator.
        
        Args:
            scraper: Instance of SenateDisclosureScraper to use
            year: Year to search for trades (defaults to current year)
            test_mode: If True, only return one trade (for testing)
            
        Returns:
            List of trade dictionaries, each containing filing details and PDF URL
        """
        disclosures = self.get_disclosures(scraper, year, test_mode=test_mode)
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