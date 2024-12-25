"""Shared pytest fixtures and configuration."""

import os
import pytest
from dotenv import load_dotenv

def pytest_configure(config):
    """Load environment variables before running tests."""
    load_dotenv()

@pytest.fixture(scope="session", autouse=True)
def check_api_key():
    """Check if API key is available before running tests."""
    api_key = os.getenv("CONGRESS_API_KEY")
    if not api_key:
        pytest.skip("CONGRESS_API_KEY environment variable not set") 