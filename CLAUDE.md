# CLAUDE.md - AI Assistant Guide for CapitolGains

## Project Overview

CapitolGains is a Python package for programmatically accessing and analyzing financial disclosure data from members of the United States Congress. It provides automated access to both House of Representatives and Senate trading activity through official government disclosure portals.

**Key capabilities:**
- Retrieve financial disclosures (PTRs, annual reports, amendments, blind trusts, extensions)
- Download disclosure PDFs
- Access Congress member data via Congress.gov API
- Web scraping with Playwright for browser automation

## Repository Structure

```
CapitolGains/
├── capitolgains/              # Main package
│   ├── __init__.py           # Package exports: Congress, Representative, Senator
│   ├── core/                 # Core business logic
│   │   ├── __init__.py       # Exports Congress, CongressMember
│   │   ├── congress.py       # Congress.gov API client
│   │   ├── representative.py # House member disclosure handling
│   │   └── senator.py        # Senate member disclosure handling
│   └── utils/                # Utility modules
│       ├── __init__.py
│       ├── representative_scraper.py  # House disclosure portal scraper
│       └── senator_scraper.py         # Senate disclosure portal scraper
├── tests/                    # Test suite
│   ├── conftest.py          # Pytest fixtures
│   ├── test_core/           # Core functionality tests
│   ├── test_house/          # House-specific tests
│   ├── test_senate/         # Senate-specific tests
│   └── test_utils/          # Utility tests
├── examples/                 # Usage examples
│   └── congress_disclosure_example.py
├── pyproject.toml           # Package configuration
├── requirements.txt         # Dependencies
├── pytest.ini              # Test configuration
└── .env.example            # Environment template
```

## Key Classes and Architecture

### Core Classes

1. **`Congress`** (`capitolgains/core/congress.py`)
   - Client for Congress.gov API
   - Retrieves member data for any congress number
   - Handles pagination and API authentication
   - Uses `CONGRESS_API_KEY` environment variable

2. **`Representative`** (`capitolgains/core/representative.py`)
   - Handles House member financial disclosures
   - Supports records from 1995 onwards
   - Uses `HouseDisclosureScraper` for data retrieval
   - Caches disclosure results per year

3. **`Senator`** (`capitolgains/core/senator.py`)
   - Handles Senate member financial disclosures
   - Supports records from 2012 onwards
   - Uses `SenateDisclosureScraper` for data retrieval
   - More report type categories than House

### Scraper Classes

4. **`HouseDisclosureScraper`** (`capitolgains/utils/representative_scraper.py`)
   - Scrapes https://disclosures-clerk.house.gov
   - Uses Playwright for browser automation
   - Context manager pattern (`with` statement)
   - All disclosures are PDFs

5. **`SenateDisclosureScraper`** (`capitolgains/utils/senator_scraper.py`)
   - Scrapes https://efdsearch.senate.gov
   - Requires accepting terms before searching
   - Handles both web tables and PDF filings
   - DataTables-based pagination

### Enums

- **`ReportType`** (`representative_scraper.py`): PTR, ANNUAL, AMENDMENT, BLIND_TRUST, EXTENSION, NEW_FILER, TERMINATION, OTHER

## Development Setup

### Prerequisites
- Python 3.8+
- Playwright browsers

### Installation

```bash
# Clone and setup virtual environment
git clone https://github.com/thewillmundy/capitolgains.git
cd capitolgains
python -m venv venv
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

# Setup environment
cp .env.example .env
# Edit .env with your CONGRESS_API_KEY from https://api.congress.gov/
```

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `CONGRESS_API_KEY` | Yes (for Congress class) | API key from congress.gov |
| `HEADLESS` | No | Run browser headless (default: true) |
| `LOG_LEVEL` | No | Logging level (DEBUG, INFO, WARNING, ERROR) |
| `DOWNLOAD_DIR` | No | Directory for downloaded files |

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run by category
pytest tests/test_house/     # House-specific tests
pytest tests/test_senate/    # Senate-specific tests
pytest tests/test_core/      # Core functionality tests
pytest tests/test_utils/     # Utility function tests

# Run by marker
pytest -m house              # House-related tests
pytest -m senate             # Senate-related tests
pytest -m integration        # Tests requiring external services
pytest -m scraper            # Scraper-specific tests
pytest -m core               # Core functionality tests
```

### Test Markers (defined in pytest.ini)

- `senate` - Senate-related functionality
- `house` - House-related functionality
- `scraper` - Web scraping functionality
- `core` - Core functionality
- `integration` - Tests requiring external services
- `slow` - Long-running tests

### Key Test Fixtures (conftest.py)

- `api_key` - Congress.gov API key from environment
- `senate_scraper` - SenateDisclosureScraper instance
- `house_scraper` - HouseDisclosureScraper instance
- `test_senators` - List of test senators with known data
- `test_representatives` - List of test representatives with known data
- `future_year` - Year in the future (for validation tests)

## Code Conventions

### Patterns

1. **Context Managers**: Both scrapers use `with` statement for resource management
   ```python
   with HouseDisclosureScraper(headless=True) as scraper:
       results = scraper.search_member_disclosures(...)
   ```

2. **Caching**: Both `Representative` and `Senator` cache disclosure results in `_cached_disclosures` dict

3. **Validation**: Input validation happens early (state codes, years, dates)
   - House: years 1995+ valid
   - Senate: years 2012+ valid
   - Both: future years invalid

4. **Method Chaining**: `with_session()` returns `self` for chaining

### Disclosure Data Structure

Both House and Senate return categorized disclosures:
```python
{
    'trades': [...],      # PTRs (Periodic Transaction Reports)
    'annual': [...],      # Annual financial disclosures
    'amendments': [...],  # Amendments to filings
    'blind_trust': [...], # Blind trust reports
    'extension': [...],   # Filing extensions
    'other': [...]        # Other report types
}
```

### Error Handling

- `ValueError` - Invalid inputs, failed operations
- `TimeoutError` - Page/element didn't load in time
- `PlaywrightTimeout` - Browser automation timeouts (wrapped as TimeoutError)

### Logging

Uses Python's `logging` module with module-level loggers:
```python
logger = logging.getLogger(__name__)
```

## Common Tasks

### Adding a New Report Type

1. Add enum value to `ReportType` in `representative_scraper.py`
2. Update categorization logic in `Representative.get_disclosures()` or `Senator.get_disclosures()`
3. Update `REPORT_TYPE_MAP` in `SenateDisclosureScraper` if needed
4. Add tests for the new type

### Modifying Scraper Behavior

1. Scrapers are in `capitolgains/utils/`
2. Session management via `with_session()` method
3. Form filling uses Playwright selectors
4. Result extraction via `_extract_page_results()` or similar

### Adding Tests

1. Place in appropriate `tests/test_*` directory
2. Use appropriate markers (`@pytest.mark.house`, etc.)
3. Use fixtures from `conftest.py`
4. Integration tests should be marked `@pytest.mark.integration`

## Important Notes

### Rate Limiting
- Congress.gov API: Be mindful of rate limits
- Disclosure portals: Include delays between requests to avoid blocking

### Data Availability
- House records: 1995 onwards
- Senate records: 2012 onwards
- Current year data may be incomplete

### Browser Automation
- Playwright runs Chromium by default
- Set `headless=False` for debugging
- Downloads go to platform-specific user data directory by default

### State Codes
- House: Accepts all US states, territories (AS, GU, PR, VI, MP), and DC
- Senate: Only 50 states (no territories or DC - they don't have senators)

## Dependencies

Core:
- `requests` - HTTP client for Congress.gov API
- `playwright` - Browser automation
- `python-dotenv` - Environment variable management
- `appdirs` - Platform-specific directories

Dev/Test:
- `pytest` - Test framework
- `pytest-timeout` - Test timeouts
- `pytest-playwright` - Playwright pytest integration
