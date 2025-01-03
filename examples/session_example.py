"""Example demonstrating session handling with both House and Senate scrapers.

This example shows different ways to use session management:
1. Basic single-member usage for both chambers
2. Efficient bulk processing with session reuse
3. Handling session errors and recovery

Run with test_mode=True to see browser activity (non-headless mode).
"""

import logging
import argparse
from typing import List
from tenacity import retry, stop_after_attempt, wait_exponential

from capitolgains.core.senator import Senator
from capitolgains.core.representative import Representative
from capitolgains.utils.senator_scraper import SenateDisclosureScraper
from capitolgains.utils.representative_scraper import HouseDisclosureScraper

# Configure logging to show session info
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def process_single_members(test_mode: bool = False):
    """Example of processing individual members from both chambers."""
    logger.info("=== Single Member Example ===")
    
    # Senate example - Simple convenience method
    logger.info("\nProcessing Senator Warren (Simple Method):")
    senate_disclosures = Senator.get_member_disclosures(
        "Warren",
        first_name="Elizabeth",
        state="MA",
        year="2023",
        headless=not test_mode
    )
    logger.info(f"Found {len(senate_disclosures['trades'])} trades")
    
    # House example - Simple convenience method
    logger.info("\nProcessing Representative Pelosi (Simple Method):")
    house_disclosures = Representative.get_member_disclosures(
        "Pelosi",
        state="CA",
        district="11",
        year="2023",
        headless=not test_mode
    )
    logger.info(f"Found {len(house_disclosures['trades'])} trades")
    
    # Examples with explicit scraper management
    logger.info("\n=== Traditional Method Examples ===")
    
    # Senate example - Traditional method
    with SenateDisclosureScraper(headless=not test_mode) as senate_scraper:
        senator = Senator("Warren", first_name="Elizabeth", state="MA")
        logger.info("\nProcessing Senator Warren (Traditional Method):")
        disclosures = senator.get_disclosures(senate_scraper, "2023")
        logger.info(f"Found {len(disclosures['trades'])} trades")
    
    # House example - Traditional method
    with HouseDisclosureScraper(headless=not test_mode) as house_scraper:
        rep = Representative("Pelosi", state="CA", district="11")
        logger.info("\nProcessing Representative Pelosi (Traditional Method):")
        disclosures = rep.get_disclosures(house_scraper, "2023")
        logger.info(f"Found {len(disclosures['trades'])} trades")

def process_multiple_members(test_mode: bool = False):
    """Example of efficiently processing multiple members with session reuse."""
    logger.info("\n=== Multiple Members Example (Session Reuse) ===")
    
    # Senate example with multiple members
    senators = [
        Senator("Warren", first_name="Elizabeth", state="MA"),
        Senator("Sanders", first_name="Bernard", state="VT"),
        Senator("Schumer", first_name="Charles", state="NY")
    ]
    
    logger.info("\nProcessing multiple senators:")
    senate_results = {}
    
    with SenateDisclosureScraper(headless=not test_mode) as senate_scraper:
        for senator in senators:
            try:
                logger.info(f"Processing {senator.first_name} {senator.name}")
                senate_results[senator] = senator.get_disclosures(senate_scraper, "2023")
                total = sum(len(v) for v in senate_results[senator].values())
                logger.info(f"Found {total} total disclosures")
            except Exception as e:
                logger.error(f"Error processing {senator.name}: {e}")
                
                # Option 1: Skip and continue with next senator (current implementation)
                senate_results[senator] = {
                    'trades': [], 'annual': [], 'amendments': [],
                    'blind_trust': [], 'extension': [], 'other': []
                }
                
                # Option 2: Retry with new session
                # try:
                #     logger.info("Forcing new session and retrying...")
                #     senate_scraper.with_session(force_new=True)
                #     senate_results[senator] = senator.get_disclosures(senate_scraper, "2023")
                # except Exception as retry_e:
                #     logger.error(f"Retry failed: {retry_e}")
                #     senate_results[senator] = {
                #         'trades': [], 'annual': [], 'amendments': [],
                #         'blind_trust': [], 'extension': [], 'other': []
                #     }
                
                # Option 3: Fail fast
                # raise  # Stop processing on first error
                
                # Option 4: Use tenacity for retries (see demonstrate_session_recovery)
                # @retry(stop=stop_after_attempt(3), wait=wait_exponential(...))
                # def process_with_retry(scraper, senator):
                #     try:
                #         return senator.get_disclosures(scraper, "2023")
                #     except Exception:
                #         scraper.with_session(force_new=True)
                #         raise
    
    # House example with multiple members
    representatives = [
        Representative("Pelosi", state="CA", district="11"),
        Representative("Johnson", state="LA", district="4"),
        Representative("Ocasio-Cortez", state="NY", district="14")
    ]
    
    logger.info("\nProcessing multiple representatives:")
    house_results = {}
    
    with HouseDisclosureScraper(headless=not test_mode) as house_scraper:
        for rep in representatives:
            try:
                logger.info(f"Processing {rep.name}")
                house_results[rep] = rep.get_disclosures(house_scraper, "2023")
                total = sum(len(v) for v in house_results[rep].values())
                logger.info(f"Found {total} total disclosures")
            except Exception as e:
                logger.error(f"Error processing {rep.name}: {e}")
                
                # Option 1: Skip and continue (current implementation)
                house_results[rep] = {'trades': [], 'annual': []}
                
                # Option 2: Retry with new session
                # try:
                #     logger.info("Forcing new session and retrying...")
                #     house_scraper.with_session(force_new=True)
                #     house_results[rep] = rep.get_disclosures(house_scraper, "2023")
                # except Exception as retry_e:
                #     logger.error(f"Retry failed: {retry_e}")
                #     house_results[rep] = {'trades': [], 'annual': []}
                
                # Option 3: Fail fast
                # raise  # Stop processing on first error

def demonstrate_session_recovery(test_mode: bool = False):
    """Example showing how to handle session errors and retries."""
    logger.info("\n=== Session Recovery Example ===")
    
    # Define retry decorators for both chambers
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        reraise=True
    )
    def process_senator(scraper, senator, year):
        """Process a senator with automatic retries using tenacity."""
        try:
            return senator.get_disclosures(scraper, year)
        except Exception as e:
            logger.warning(f"Attempt failed for {senator.name}: {e}")
            scraper.with_session(force_new=True)  # Force new session before retry
            raise  # Let tenacity handle the retry
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        reraise=True
    )
    def process_representative(scraper, rep, year):
        """Process a representative with automatic retries using tenacity."""
        try:
            return rep.get_disclosures(scraper, year)
        except Exception as e:
            logger.warning(f"Attempt failed for {rep.name}: {e}")
            scraper.with_session(force_new=True)  # Force new session before retry
            raise  # Let tenacity handle the retry
    
    # Test error handling with invalid members
    test_senators = [
        Senator("Warren", first_name="Elizabeth", state="MA"),
        Senator("NonexistentSenator", first_name="Invalid", state="XX")
    ]
    
    test_representatives = [
        Representative("Pelosi", state="CA", district="11"),
        Representative("NonexistentRep", state="XX", district="99")
    ]
    
    # Process senators with retry logic
    logger.info("\nTesting Senate retry strategy:")
    with SenateDisclosureScraper(headless=not test_mode) as senate_scraper:
        for senator in test_senators:
            try:
                disclosures = process_senator(senate_scraper, senator, "2023")
                total = sum(len(v) for v in disclosures.values())
                logger.info(f"{senator.name}: Found {total} total disclosures")
            except Exception as e:
                logger.error(f"All retries failed for {senator.name}: {e}")
    
    # Process representatives with retry logic
    logger.info("\nTesting House retry strategy:")
    with HouseDisclosureScraper(headless=not test_mode) as house_scraper:
        for rep in test_representatives:
            try:
                disclosures = process_representative(house_scraper, rep, "2023")
                total = sum(len(v) for v in disclosures.values())
                logger.info(f"{rep.name}: Found {total} total disclosures")
            except Exception as e:
                logger.error(f"All retries failed for {rep.name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run session management examples')
    parser.add_argument('--test-mode', action='store_true', help='Run in test mode (non-headless)')
    args = parser.parse_args()
    
    # Run examples
    process_single_members(test_mode=args.test_mode)
    process_multiple_members(test_mode=args.test_mode)
    demonstrate_session_recovery(test_mode=args.test_mode) 