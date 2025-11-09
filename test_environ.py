import os
import pytest
@pytest.fixture
def environ(request):
    return request.config.getoption("--env")
def test_check_env(environ):
    assert environ in ("dev","stage","prod")
# if i dont pass any --env it takes dafulat as dev as i have passed it in confftest.py
# 
#    
