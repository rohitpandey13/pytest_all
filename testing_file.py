import pytest
import pytest_praveen_parametrize

@pytest.mark.parametrize("a,b,expected", [(2,3,5), (5,7,12), (0,0,0)])
def test_add(a, b, expected):
    assert pytest_praveen_parametrize.add(a, b) == expected

