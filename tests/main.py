import pytest
from src import main

def test_assert_hi():
    assert 'Hi, PyCharm' == main.print_hi('PyCharm')