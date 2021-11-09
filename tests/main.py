import pytest
from src import main

def test_assert_hi():
    assert 'Hi, PyCharm' == main.print_hi('PyCharm')

def test_customer_success_balancing_method_exists_and_is_callable():
    assert "customer_success_balancing" in dir(main) and callable(main.customer_success_balancing)

