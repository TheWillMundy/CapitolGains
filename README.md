# CapitolGains

A Python package for retrieving and analyzing financial disclosure data from members of Congress. CapitolGains provides programmatic access to both Senate and House trading activity and financial disclosures through official government websites.

## Features

### Core Functionality
- Comprehensive congress member database with party affiliations
- Automated retrieval of financial disclosures:
  - Individual trade reports (Periodic Transaction Reports)
  - Annual financial disclosure forms
- Support for both Senate and House websites using Playwright
- Trade history display for current year (including previous year during grace period through February 15th)

### Upcoming Features
- Historical data tracking (years in office)
- Net worth dashboard integrating annual disclosures and recent trades
- Database integration for persistent storage
- Advanced trade history visualization
- Configurable automated data collection:
  - Filtering by individual names
  - Party-based selection
  - Chamber-specific queries (Senate/House)
  - Custom group definitions

## Installation

```bash
pip install capitolgains
```

## Usage

```python
from capitolgains import Congress, Representative, Senator

# Initialize Congress tracker
congress = Congress()

# Get all current members
members = congress.get_all_members()

# Get trades for a specific senator
senator = Senator("Warren")
trades = senator.get_recent_trades()

# Get annual disclosure for house member
rep = Representative("Pelosi")
disclosure = rep.get_annual_disclosure(2023)
```

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

This package is for educational and research purposes only. Users are responsible for ensuring compliance with all applicable laws and regulations regarding the collection and use of congressional financial data.