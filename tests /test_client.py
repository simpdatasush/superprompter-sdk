import pytest

def test_import():
    # This checks if the package is actually installed in the environment
    try:
        from superprompter import SuperPrompter
        assert True
    except ImportError:
        pytest.fail("SDK not found. Check if 'pip install -e .' ran and __init__.py exists.")

def test_sdk_initialization():
    from superprompter import SuperPrompter
    sdk = SuperPrompter(api_key="test_key")
    assert sdk.api_key == "test_key"
    assert sdk.base_url == "https://promptsgenerator.ai"


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
