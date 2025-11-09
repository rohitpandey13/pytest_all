import pytest

@pytest.mark.smoke
def test_addition_basic():    
    assert True

@pytest.mark.slow
def test_multiplication_basic():
    assert True