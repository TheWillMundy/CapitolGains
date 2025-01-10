# CapitolGains

[![PyPI version](https://badge.fury.io/py/capitolgains.svg)](https://badge.fury.io/py/capitolgains)
[![Python Support](https://img.shields.io/pypi/pyversions/capitolgains.svg)](https://pypi.org/project/capitolgains/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

CapitolGains is a robust Python package for programmatically accessing and analyzing financial disclosure data from members of the United States Congress. It provides reliable, automated access to both House and Senate trading activity and financial disclosures through official government websites.

## Features

### Data Access
- **Comprehensive Member Database**: Access details of all current Congress members with party affiliations
- **Multiple Disclosure Types**:
  - Periodic Transaction Reports (PTRs)
  - Annual Financial Disclosures
  - Blind Trust Reports
  - Filing Extensions
- **Smart Data Retrieval**:
  - Efficient caching to minimize network requests
  - Automated session management
  - Robust error handling and retries
  - Smart pagination for large result sets

### Platform Support
- **House of Representatives**:
  - Full support for House disclosure portal
  - Records available from 1995 onwards
  - Automated form submission and result parsing
- **Senate**:
  - Complete Senate disclosure system integration
  - Records available from 2012 onwards
  - Automated agreement acceptance
  - Support for both web tables and PDFs

### Data Processing
- **Flexible Search Options**:
  - Case-insensitive member matching
  - State and district filtering
  - Date range queries
  - Report type filtering
- **Rich Data Extraction**:
  - Structured data from web tables
  - Automated PDF downloads
  - Metadata parsing
  - Trade categorization

## Installation

```bash
# Install the package
pip install capitolgains

# Install browser automation dependencies
playwright install
```

## Quick Start

```python
from capitolgains import Representative, Senator
from capitolgains.utils.representative_scraper import HouseDisclosureScraper
from capitolgains.utils.senator_scraper import SenateDisclosureScraper

# House member example
with HouseDisclosureScraper() as house_scraper:
    pelosi = Representative("Pelosi", state="CA", district="11")
    disclosures = pelosi.get_disclosures(house_scraper, year="2023")

# Senate member example
with SenateDisclosureScraper() as senate_scraper:
    warren = Senator("Warren", first_name="Elizabeth", state="MA")
    disclosures = warren.get_disclosures(senate_scraper, year="2023")
```

## Advanced Usage

### Custom Search Parameters

```python
from capitolgains import Representative
from capitolgains.utils.representative_scraper import HouseDisclosureScraper, ReportType

with HouseDisclosureScraper() as scraper:
    rep = Representative("Pelosi", state="CA", district="11")
    
    # Search using ReportType enums for precise filtering
    results = rep.get_disclosures(
        scraper,
        year="2023",
        report_types=[
            ReportType.PTR,           # Periodic Transaction Reports
            ReportType.AMENDMENT,     # Amendments to filings
            ReportType.ANNUAL,        # Annual financial disclosures
            ReportType.BLIND_TRUST,   # Blind trust reports
            ReportType.EXTENSION,     # Filing extensions
            ReportType.NEW_FILER,     # New filer reports
            ReportType.TERMINATION    # Termination reports
        ]
    )
    
    # Get only trades and amendments
    trade_results = rep.get_disclosures(
        scraper,
        year="2023",
        report_types=[ReportType.PTR, ReportType.AMENDMENT]
    )
```

### Efficient Bulk Processing

```python
# Process multiple members efficiently by reusing scraper session
with SenateDisclosureScraper() as scraper:
    senators = [
        Senator("Warren", first_name="Elizabeth", state="MA"),
        Senator("Sanders", first_name="Bernard", state="VT"),
        Senator("Tuberville", first_name="Tommy", state="AL")
    ]
    
    for senator in senators:
        try:
            # Get trades for a specific date range
            disclosures = senator.get_disclosures(
                scraper,
                start_date="01/01/2023",
                end_date="12/31/2023"
            )
            trades = disclosures['trades']
            print(f"Found {len(trades)} trades for {senator.name}")
        except Exception as e:
            # If session expires, force a new one
            scraper.with_session(force_new=True)
```

### Congress Member Database

```python
from capitolgains import Congress

# Initialize Congress tracker with API key
congress = Congress(api_key="your_api_key")  # Get key from congress.gov/api

# Get all members of the current Congress (automatically uses current session)
members = congress.get_all_members()

# Process members by chamber
house_members = [m for m in members if m.chamber == 'House']
senate_members = [m for m in members if m.chamber == 'Senate']

# Use member data directly
with HouseDisclosureScraper() as house_scraper:
    # Process first 3 House members
    for member in house_members[:3]:
        # Extract member details
        last_name = member.name.split()[-1]
        state = member.state
        
        # Create Representative instance and get disclosures
        rep = Representative(last_name, state=state)
        disclosures = rep.get_disclosures(house_scraper, year="2023")
        print(f"Found {len(disclosures['trades'])} trades for {member.name}")

with SenateDisclosureScraper() as senate_scraper:
    # Process first 3 Senators
    for member in senate_members[:3]:
        # Extract member details
        name_parts = member.name.split()
        first_name = name_parts[0]
        last_name = name_parts[-1]
        state = member.state
        
        # Create Senator instance and get disclosures
        sen = Senator(last_name, first_name=first_name, state=state)
        disclosures = sen.get_disclosures(senate_scraper, year="2023")
        print(f"Found {len(disclosures['trades'])} trades for {member.name}")
```

## Development

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/capitolgains.git
cd capitolgains
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r tests/requirements-test.txt
```

### Running Tests

The project includes comprehensive test suites:

```bash
# Run all tests
pytest

# Run specific test categories
pytest tests/test_house/  # House-specific tests
pytest tests/test_senate/  # Senate-specific tests
pytest tests/test_core/   # Core functionality tests
pytest tests/test_utils/  # Utility function tests

# Run with specific markers
pytest -m "house"        # House-related tests
pytest -m "senate"       # Senate-related tests
pytest -m "integration"  # Integration tests
pytest -m "scraper"      # Scraper-specific tests
```

### Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for your changes
5. Ensure all tests pass
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This package is for educational and research purposes only. Users are responsible for ensuring compliance with all applicable laws and regulations regarding the collection and use of congressional financial data. This project is not affiliated with, endorsed by, or sponsored by the United States Congress or any government agency.

## Acknowledgments

- Data sourced from official House and Senate disclosure portals
- Congress member data from [Congress.gov API](https://api.congress.gov/)