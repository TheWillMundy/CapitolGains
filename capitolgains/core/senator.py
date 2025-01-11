"""Senate financial disclosure functionality.

This module provides functionality to retrieve and process financial disclosures for
Senators. It handles:
- Searching and retrieving financial disclosures
- Caching disclosure data to minimize network requests
- Filtering and categorizing disclosures by type
- Downloading disclosure PDFs

The Senate disclosure system has specific requirements and limitations:
- Electronic records are available from 2012 onwards
- Requires accepting terms before searching
- Uses a different categorization system than the House
- Includes additional report types (blind trusts, extensions)
"""

from datetime import datetime
from typing import List, Dict, Any, Optional, ClassVar, Set
from capitolgains.utils.senator_scraper import SenateDisclosureScraper
import logging

logger = logging.getLogger(__name__)

class Senator:
    """A Senator and their financial disclosures.
    
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
        VALID_STATES: Set of valid two-letter state codes (excludes territories and DC)
    """
    
    VALID_STATES: ClassVar[Set[str]] = {
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
    }

    @classmethod
    def validate_state(cls, state: Optional[str]) -> None:
        """Validate that a state code is valid for Senate searches.
        
        Args:
            state: Two-letter state code to validate, or None
            
        Raises:
            ValueError: If the state code is invalid
            
        Note:
            The Senate state list is more limited than the House list because:
            - Territories (AS, GU, PR, VI, MP) don't have Senate representation
            - DC doesn't have Senate representation
            - Only the 50 states have Senate representation
        """
        if state is not None and state not in cls.VALID_STATES:
            valid_states = ', '.join(sorted(cls.VALID_STATES))
            raise ValueError(
                f"Invalid state code for Senate: {state}. Must be one of: {valid_states}"
            )
    
    @classmethod
    def get_member_disclosures(
        cls,
        name: str,
        year: Optional[str] = None,
        first_name: Optional[str] = None,
        state: Optional[str] = None,
        headless: bool = True,
        include_candidate_reports: bool = False,
        test_mode: bool = False
    ) -> Dict[str, List[Dict[str, Any]]]:
        """Get financial disclosures for a single senator.
        
        This method handles the scraper lifecycle management for simple single-member
        queries. For bulk processing of multiple senators, use the scraper's
        process_members method instead.
        
        Args:
            name: Senator's last name
            year: Year to search for (defaults to current year)
            first_name: Senator's first name (optional)
            state: Two-letter state code (optional)
            headless: Whether to run browser in headless mode
            include_candidate_reports: Whether to include candidate reports
            test_mode: If True, only return one match per category
            
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
            
        Example:
            ```python
            # Simple single-member usage
            disclosures = Senator.get_member_disclosures("Warren", year="2023")
            ```
        """
        # Validate state before creating scraper
        cls.validate_state(state)
        
        with SenateDisclosureScraper(headless=headless) as scraper:
            senator = cls(name, first_name=first_name, state=state)
            return senator.get_disclosures(
                scraper,
                year=year,
                include_candidate_reports=include_candidate_reports,
                test_mode=test_mode
            )
    
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
        self.__class__.validate_state(state)  # Validate state on initialization
        self.state = state
        self._cached_disclosures: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
        
    @staticmethod
    def validate_year(year: str) -> None:
        """Validate that a year is valid for searching.
        
        Args:
            year: Year string to validate
            
        Raises:
            ValueError: If the year is invalid or in an invalid format
            
        Note:
            - Years must be 2012 or later (when electronic records began)
            - Only strictly future years are invalid
        """
        try:
            year_int = int(year)
            current_year = datetime.now().year
            
            if year_int < 2012:  # Senate electronic records start from 2012
                raise ValueError(f"Year must be 2012 or later, got {year}")
            if year_int > current_year:  # Only block strictly future years
                raise ValueError(f"Year cannot be in the future (current year is {current_year}), got {year}")
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                raise ValueError(f"Invalid year format: {year}. Must be a valid year number.")
            raise

    def get_disclosures(
        self, 
        scraper: SenateDisclosureScraper, 
        year: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        include_candidate_reports: bool = False,
        test_mode: bool = False
    ) -> Dict[str, List[Dict[str, Any]]]:
        """Get all disclosures for the senator for a given year or date range.
        
        This method fetches all types of financial disclosures for the specified period:
        - Periodic Transaction Reports (PTRs)
        - Annual Financial Disclosures (FDs)
        - Blind Trust Reports
        - Filing Extensions
        - Other Documents
        
        Results are cached to minimize network requests.
        
        Args:
            scraper: Instance of SenateDisclosureScraper to use for fetching data
            year: Year to search for (defaults to current year if no dates provided)
            start_date: Optional start date in MM/DD/YYYY format
            end_date: Optional end date in MM/DD/YYYY format
            include_candidate_reports: Whether to include candidate reports
            test_mode: If True, only return one match per category
            
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
            
        Note:
            Date handling:
            - If start_date/end_date are provided, they take precedence over year
            - If only year is provided, it will search the entire year
            - If no dates are provided, defaults to current year
            - Only reports from 2012 onwards are available
            - end_date requires start_date to be provided
            
        Raises:
            ValueError: If end_date is provided without start_date
        """
        if not year and not start_date and not end_date:
            year = str(datetime.now().year)
            
        # Validate that if end_date is provided, start_date must also be provided
        if end_date and not start_date:
            raise ValueError("end_date requires start_date")
            
        # Create a cache key that includes all search parameters
        cache_key = f"{year}_{start_date}_{end_date}_{include_candidate_reports}_{test_mode}"
        
        if cache_key in self._cached_disclosures:
            return self._cached_disclosures[cache_key]
            
        # Fetch all disclosure types in one request
        all_disclosures = scraper.search_member_disclosures(
            last_name=self.name,
            filing_year=year if not (start_date or end_date) else None,
            first_name=self.first_name,
            state=self.state,
            report_types=['annual', 'ptr', 'extension', 'blind_trust', 'other'],
            include_candidate_reports=include_candidate_reports,
            start_date=start_date,
            end_date=end_date
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
                if not test_mode or len(categorized['extension']) == 0:
                    categorized['extension'].append(disclosure)
                continue
                
            if 'amendment' in report_type:
                if not test_mode or len(categorized['amendments']) == 0:
                    categorized['amendments'].append(disclosure)
                continue
                
            # Then check other categories
            if 'periodic transaction' in report_type:
                if not test_mode or len(categorized['trades']) == 0:
                    categorized['trades'].append(disclosure)
            elif ('annual report for cy' in report_type or
                  'financial disclosure report' in report_type or 
                  'public financial disclosure' in report_type or
                  report_type == 'annual report'):
                if not test_mode or len(categorized['annual']) == 0:
                    categorized['annual'].append(disclosure)
            elif 'blind trust' in report_type:
                if not test_mode or len(categorized['blind_trust']) == 0:
                    categorized['blind_trust'].append(disclosure)
            else:
                if not test_mode or len(categorized['other']) == 0:
                    categorized['other'].append(disclosure)
        
        # Cache results with the combined key
        self._cached_disclosures[cache_key] = categorized
        return categorized
        
    def _matches_senator(self, disclosure: Dict[str, Any]) -> bool:
        """Check if a disclosure matches this senator's details.
        
        Args:
            disclosure: Disclosure dictionary from search results
            
        Returns:
            True if the disclosure matches this senator's details
            
        Note:
            We only check names here because:
            1. State is already validated during Senator initialization
            2. State is used in the search form to filter results
            3. Office field format can vary, making state matching unreliable
        """
        # Check last name first (most reliable)
        if disclosure['last_name'].lower() != self.name.lower():
            return False
            
        # Check first name if provided with leniency
        if self.first_name and disclosure.get('first_name'):
            disclosure_first = disclosure['first_name'].lower()
            our_first = self.first_name.lower()
            # Accept if either name starts with the other
            if not (disclosure_first.startswith(our_first) or our_first.startswith(disclosure_first)):
                return False
        
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