import pytest
from superprompter import SuperPrompter

def test_sdk_initialization():
    sdk = SuperPrompter(api_key="test_key", base_url="https://test.com")
    assert sdk.api_key == "test_key"
    assert sdk.headers["X-API-KEY"] == "test_key"

def test_search_params():
    # This tests if the logic correctly handles empty queries
    sdk = SuperPrompter(api_key="test_key")
    # We expect a dict return even on failure
    results = sdk.search_news(query="") 
    assert isinstance(results, dict)
