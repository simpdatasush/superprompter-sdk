import sys
import os
import pytest

# Manually add src to path within the test as a fail-safe
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_import_superprompter():
    """Verify that the package is installable and the class is importable."""
    try:
        from superprompter import SuperPrompter
        sdk = SuperPrompter(api_key="test_key")
        assert sdk.api_key == "test_key"
        assert "X-API-KEY" in sdk.headers
    except ImportError as e:
        pytest.fail(f"Could not import SuperPrompter. Error: {e}")

def test_search_news_method_exists():
    """Verify that the search_news method is available on the class."""
    from superprompter import SuperPrompter
    sdk = SuperPrompter(api_key="test")
    assert hasattr(sdk, 'search_news')
    assert callable(sdk.search_news)
