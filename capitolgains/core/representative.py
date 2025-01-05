"""House Representative functionality.

This module provides the Representative class for managing House Representative data
and their financial disclosures. It handles caching of disclosure data and provides
methods to fetch both periodic transaction reports (PTRs) and annual financial disclosures.
"""

from datetime import datetime
from typing import List, Dict, Any, Optional, ClassVar
from capitolgains.utils.representative_scraper import HouseDisclosureScraper
import logging

logger = logging.getLogger(__name__)

class Representative:
    """Class representing a House Representative and their financial disclosures.
    
    This class provides functionality to:
    - Search and retrieve financial disclosures
    - Cache disclosure data to minimize network requests
    - Filter and categorize disclosures by type (trades vs annual reports)
    - Download disclosure PDFs
    
    Attributes:
        name: Representative's last name used for searches
        state: Two-letter state code (optional)
        district: District number (optional)
        _cached_disclosures: Internal cache mapping years to disclosure data
    """
    
    @classmethod
    def get_member_disclosures(
        cls,
        name: str,
        year: Optional[str] = None,
        state: Optional[str] = None,
        district: Optional[str] = None,
        headless: bool = True
    ) -> Dict[str, List[Dict[str, Any]]]:
        """Convenience method for single-member queries.
        
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
                'annual': List of annual disclosures (FD)
            }
            
        Example:
            ```python
            # Simple single-member usage
            disclosures = Representative.get_member_disclosures(
                "Pelosi", state="CA", district="11", year="2023"
            )
            ```
        """
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
                'annual': List of annual disclosures (FD)
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
        
        # Log filing types for debugging
        logger.info("Filing types found:")
        for d in filtered_disclosures:
            logger.info(f"Filing type: {d['filing_type']}")
        
        # Categorize disclosures by type
        categorized = {
            'trades': [d for d in filtered_disclosures if 'PTR' in d['filing_type']],
            'annual': [d for d in filtered_disclosures if 'FD' in d['filing_type']]
        }
        
        # Log categorization results
        logger.info(f"Categorized {len(filtered_disclosures)} disclosures:")
        logger.info(f"- Trades: {len(categorized['trades'])}")
        logger.info(f"- Annual: {len(categorized['annual'])}")
        
        # Cache the results
        self._cached_disclosures[year] = categorized
        return categorized
        
    def _matches_representative(self, disclosure: Dict[str, Any]) -> bool:
        """Check if a disclosure matches this representative's details.
        
        Args:
            disclosure: Disclosure dictionary from search results
            
        Returns:
            True if the disclosure matches this representative's details
        """
        logger.info(f"Checking disclosure: {disclosure}")
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
                    logger.warning(f"Invalid office format: {office}")
                    return False
            
            # If state is specified and doesn't match, return False
            if self.state and disc_state != self.state:
                logger.warning(f"State mismatch: {disc_state} != {self.state}")
                return False
                
            # If district is specified and doesn't match, return False
            if self.district and disc_district != self.district:
                logger.warning(f"District mismatch: {disc_district} != {self.district}")
                return False
                
            # If we got here and had either state or district specified, it's a match
            logger.info("Disclosure matches representative by office")
            return True
            
        # If we get here, either:
        # 1. We don't have state/district info to match against
        # 2. Office wasn't present in the disclosure
        # In these cases, we just verify the name matches
        name = disclosure.get('name', '').lower()
        if not name:
            logger.warning("No name found in disclosure")
            return False
            
        # Simple case-insensitive check if the last name appears in the full name
        if self.name.lower() not in name:
            logger.warning(f"Name mismatch: {self.name} not found in {name}")
            return False
            
        logger.info("Disclosure matches representative by name")
        return True
        
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