import pytest
from superprompter import SuperPrompter

def test_sdk_init():
    """Check if the class initializes with the correct key."""
    sdk = SuperPrompter(api_key="test_123")
    assert sdk.api_key == "test_123"

def test_sdk_endpoint():
    """Check if the default URL is correct."""
    sdk = SuperPrompter(api_key="test")
    assert "promptsgenerator.ai" in sdk.base_url
