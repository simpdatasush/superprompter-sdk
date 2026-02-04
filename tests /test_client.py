import pytest
from superprompter import SuperPrompter

def test_sdk_defaults():
    # Test that if we don't provide a URL, it uses your real domain
    sdk = SuperPrompter(api_key="test_key")
    assert sdk.base_url == "https://promptsgenerator.ai"

def test_sdk_initialization():
    # Test that parameters are assigned to the right headers
    sdk = SuperPrompter(api_key="sp_123", base_url="https://test.com")
    assert sdk.api_key == "sp_123"
    assert sdk.headers["X-API-KEY"] == "sp_123"

def test_search_logic_error_handling():
    # This tests how the SDK handles a completely fake URL
    # It should return an error dict rather than crashing the program
    sdk = SuperPrompter(api_key="test_key", base_url="https://invalid.url.that.does.not.exist")
    results = sdk.search_news(query="test")
    assert "error" in results
