"""Example demonstrating how to pull congress information and process disclosures.

This example shows:
1. Getting current congress members using the Congress.gov API
2. Processing specific members (Tuberville, Blumenthal, and Pelosi)
3. Downloading and saving specific report types
4. Generating a summary of disclosures
"""

import os
import json
from datetime import datetime
from pathlib import Path
import logging
from typing import Dict, List, Any
from tabulate import tabulate

from capitolgains import Congress, Senator, Representative
from capitolgains.utils.senator_scraper import SenateDisclosureScraper
from capitolgains.utils.representative_scraper import HouseDisclosureScraper, ReportType
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def setup_output_dir() -> Path:
    """Create and return output directory for saving files."""
    output_dir = Path("outputs")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir

def process_senator_disclosures(
    senator: Senator,
    scraper: SenateDisclosureScraper,
    year: str,
    output_dir: Path
) -> Dict[str, int]:
    """Process disclosures for a senator."""
    disclosures = senator.get_disclosures(scraper, year=year)
    counts = {
        'annual': len(disclosures.get('annual', [])),
        'amendments': len(disclosures.get('amendments', [])),
        'trades': len(disclosures.get('trades', []))
    }
    
    member_dir = output_dir / f"senate_{senator.name.lower()}"
    member_dir.mkdir(exist_ok=True)
    
    # Process annual report
    if disclosures.get('annual'):
        try:
            scraper.with_session(force_new=True)
            result = scraper.process_filing(
                disclosures['annual'][0]['report_url'],
                report_type='annual',
                download_dir=str(member_dir)
            )
            if result.get('type') == 'web_table' and result.get('metadata') and result.get('sections'):
                with open(member_dir / 'annual_report.json', 'w') as f:
                    json.dump({
                        'metadata': result['metadata'],
                        'sections': result['sections']
                    }, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to process annual report: {str(e)}")
            scraper.with_session(force_new=True)
            
    # Process trade report
    if disclosures.get('trades'):
        try:
            scraper.with_session(force_new=True)
            result = scraper.process_filing(
                disclosures['trades'][0]['report_url'],
                report_type='ptr',
                download_dir=str(member_dir)
            )
            if result.get('type') == 'web_table' and result.get('metadata') and result.get('sections'):
                with open(member_dir / 'trade_report.json', 'w') as f:
                    json.dump({
                        'metadata': result['metadata'],
                        'sections': result.get('sections', {})
                    }, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to process trade report: {str(e)}")
            scraper.with_session(force_new=True)
            
    return counts

def process_representative_disclosures(
    rep: Representative,
    scraper: HouseDisclosureScraper,
    year: str,
    output_dir: Path
) -> Dict[str, int]:
    """Process disclosures for a representative."""
    disclosures = scraper.search_member_disclosures(
        last_name=rep.name,
        filing_year=year,
        state=rep.state,
        district=rep.district,
        report_types=[ReportType.PTR, ReportType.ANNUAL, ReportType.AMENDMENT]
    )
    
    counts = {
        'annual': len([d for d in disclosures if 'annual' in d['filing_type'].lower()]),
        'amendments': len([d for d in disclosures if 'amendment' in d['filing_type'].lower()]),
        'trades': len([d for d in disclosures if 'transaction' in d['filing_type'].lower() or 'ptr' in d['filing_type'].lower()])
    }
    
    member_dir = output_dir / f"house_{rep.name.lower()}"
    member_dir.mkdir(exist_ok=True)
    
    trade_reports = [d for d in disclosures if 'transaction' in d['filing_type'].lower() or 'ptr' in d['filing_type'].lower()]
    if trade_reports:
        try:
            scraper.download_disclosure_pdf(
                trade_reports[0]['pdf_url'],
                str(member_dir)
            )
        except Exception as e:
            logger.error(f"Failed to download trade report: {str(e)}")
            
    return counts

def main():
    try:
        load_dotenv()
        api_key = os.getenv('CONGRESS_API_KEY')
        if not api_key:
            raise ValueError("Please set CONGRESS_API_KEY in .env file")
            
        output_dir = setup_output_dir()
        year = str(datetime.now().year - 1)  # Previous year
        
        members = {
            'senate': [
                Senator("Tuberville", first_name="Thomas", state="AL"),
                Senator("Blumenthal", first_name="Richard", state="CT")
            ],
            'house': [
                Representative("Pelosi", state="CA", district="11")
            ]
        }
        
        results = []
        
        # Process senators
        with SenateDisclosureScraper() as senate_scraper:
            for senator in members['senate']:
                try:
                    counts = process_senator_disclosures(
                        senator,
                        senate_scraper,
                        year,
                        output_dir
                    )
                    results.append([
                        f"Sen. {senator.name}",
                        counts['annual'],
                        counts['amendments'],
                        counts['trades']
                    ])
                except Exception as e:
                    logger.error(f"Error processing {senator.name}: {str(e)}")
                    results.append([f"Sen. {senator.name}", "Error", "Error", "Error"])
                    
        # Process house member
        with HouseDisclosureScraper() as house_scraper:
            for rep in members['house']:
                try:
                    counts = process_representative_disclosures(
                        rep,
                        house_scraper,
                        year,
                        output_dir
                    )
                    results.append([
                        f"Rep. {rep.name}",
                        counts['annual'],
                        counts['amendments'],
                        counts['trades']
                    ])
                except Exception as e:
                    logger.error(f"Error processing {rep.name}: {str(e)}")
                    results.append([f"Rep. {rep.name}", "Error", "Error", "Error"])
                    
        # Print summary table
        print("\nDisclosure Summary for", year)
        print(tabulate(
            results,
            headers=['Member', 'Annual', 'Amendments', 'Trades'],
            tablefmt='pipe'
        ))
        print(f"\nFiles saved in: {output_dir}")
        
    except Exception as e:
        logger.error(f"Script failed: {str(e)}")
        raise

if __name__ == "__main__":
    main() 