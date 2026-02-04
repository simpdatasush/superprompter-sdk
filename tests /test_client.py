import sys
import os
import pytest

# Manually add src to path within the test as a fail-safe
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_import_superprompter():
    try:
        from superprompter import SuperPrompter
        sdk = SuperPrompter(api_key="test")
        assert sdk.api_key == "test"
    except ImportError as e:
        pytest.fail(f"Could not import SuperPrompter. Error: {e}")

#import pytest
#from promptsapi import generate_prompt, reverse_prompt

#def test_generate_prompt_exists():
#   """
#   Test that the generate_prompt function can be imported and exists.
#    """
#    assert callable(generate_prompt)

#def test_reverse_prompt_exists():
#    """
#    Test that the reverse_prompt function can be imported and exists.
#    """
#    assert callable(reverse_prompt)
