import pytest
from t13_f import task

def test_task():
    assert task("qwertt", "t") == ("tt", "tt")
    assert task("qwer", "t") == (None, None)