import pytest
import os
from pathlib import Path
from dotenv import load_dotenv
from capitolgains.utils.senator_scraper import SenateDisclosureScraper
from capitolgains.utils.representative_scraper import HouseDisclosureScraper

# Load environment variables from .env file
load_dotenv()

@pytest.fixture(scope="session")
def api_key():
    """Get API key from environment variables."""
    api_key = os.getenv("CONGRESS_API_KEY")
    if not api_key:
        raise ValueError("CONGRESS_API_KEY not found in environment variables")
    return api_key

@pytest.fixture(scope="session")
def output_dir(tmp_path_factory):
    """Create a temporary directory for test outputs."""
    output_dir = tmp_path_factory.mktemp("test_outputs")
    return output_dir

@pytest.fixture(scope="function")
def senate_scraper():
    """Create a Senate scraper instance for testing."""
    with SenateDisclosureScraper(headless=True) as scraper:
        yield scraper

@pytest.fixture(scope="function")
def house_scraper():
    """Create a House scraper instance for testing."""
    with HouseDisclosureScraper(headless=True) as scraper:
        yield scraper

@pytest.fixture
def test_senators():
    """Return a list of test senators with known data."""
    return [
        ("Warren", "Elizabeth", "MA"),
        ("Sanders", "Bernard", "VT"),
        ("Tuberville", "Thomas", "AL"),
        ("Blackburn", "Marsha", "TN")
    ]

@pytest.fixture
def test_representatives():
    """Return a list of test representatives with known data."""
    return [
        ("Pelosi", "CA", "11"),
        ("Ocasio-Cortez", "NY", "14"),
        ("Johnson", "LA", "4")
    ] 