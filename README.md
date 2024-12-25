# CapitolGains

A Python package for retrieving and analyzing financial disclosure data from members of Congress. CapitolGains provides programmatic access to both Senate and House trading activity and financial disclosures through official government websites.

## Features

### Core Functionality
- [x] Comprehensive congress member database with party affiliations
- [x] Automated retrieval of financial disclosures:
  - [x] Individual trade reports (Periodic Transaction Reports)
  - [x] Annual financial disclosure forms
- [x] Support for House website using Playwright
- [x] Efficient caching of disclosure data to minimize network requests
- [x] Direct download of disclosure PDFs using HTTP requests
- [ ] Trade history display for current year (including previous year during grace period through February 15th)

### Upcoming Features
- [ ] Historical data tracking (years in office)
- [ ] Net worth dashboard integrating annual disclosures and recent trades
- [ ] Database integration for persistent storage
- [ ] Advanced trade history visualization
- [ ] Configurable automated data collection:
  - [ ] Filtering by individual names
  - [ ] Party-based selection
  - [ ] Chamber-specific queries (Senate/House)
  - [ ] Custom group definitions

## Installation

```bash
pip install capitolgains
```

## Usage

```python
from capitolgains import Congress, Representative, Senator
from capitolgains.utils.scraper import HouseDisclosureScraper

# Initialize Congress tracker
congress = Congress()

# Get all current members
members = congress.get_all_members()

# Initialize scraper
scraper = HouseDisclosureScraper()

# Get disclosures for a House member (caches results)
rep = Representative("Pelosi", state="CA", district="11")
disclosures = rep.get_disclosures(scraper, year="2023")

# Get trades for a specific year using cached data
trades_2023 = rep.get_recent_trades(scraper, year="2023")

# Get annual financial disclosure using cached data
# Returns dict with filing info and local PDF path
disclosure = rep.get_annual_disclosure(scraper, 2023)
print(f"Downloaded disclosure to: {disclosure['file_path']}")

## Project Structure
```
capitolgains/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── congress.py      # Congress member management
│   ├── representative.py # House member functionality
│   └── senator.py       # Senator functionality
├── utils/
│   ├── __init__.py
│   ├── scraper.py      # Playwright automation
│   └── parser.py       # Document parsing utilities
├── database/
│   ├── __init__.py
│   ├── models.py       # Database models
│   └── manager.py      # Database operations
└── cli/
    ├── __init__.py
    └── main.py         # Command-line interface
```

## Development Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/capitolgains.git
cd capitolgains
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers
```bash
playwright install
```

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This package is for educational and research purposes only. Users are responsible for ensuring compliance with all applicable laws and regulations regarding the collection and use of congressional financial data. This project utilizes data from various sources, including the [Congress.gov API](https://github.com/LibraryOfCongress/api.congress.gov/) and other publicly available resources.