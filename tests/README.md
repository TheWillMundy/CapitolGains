# Testing CapitolGains

This directory contains the test suite for the CapitolGains package.

## Setup

1. Install test dependencies:
```bash
pip install -r requirements-test.txt
```

2. Install the package in development mode:
```bash
pip install -e .
```

3. Set up environment variables:
The tests use the same `.env` file as the main application. Make sure you have a `.env` file in the root directory with:
```
CONGRESS_API_KEY=your_api_key_here
```

4. Install Playwright browsers:
```bash
playwright install
```

## Running Tests

Run all tests:
```bash
pytest
```

Run with coverage report:
```bash
pytest --cov=capitolgains
```

Run specific test file:
```bash
pytest tests/core/test_congress.py
```

## Test Structure

- `tests/conftest.py`: Shared pytest fixtures and configuration
- `tests/core/`: Tests for core functionality
  - `test_congress.py`: Tests for Congress API integration

## Notes

- Tests use real API calls to ensure actual functionality
- Requires valid Congress.gov API key
- Tests will be skipped if API key is not available
- Playwright is used for browser automation in tests, ensure it is set up correctly 