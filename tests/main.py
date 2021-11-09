import pytest
from src import main

def test_assert_hi():
    assert 'Hi, PyCharm' == main.print_hi('PyCharm')

def test_customer_success_balancing_method_exists_and_is_callable():
    assert "customer_success_balancing" in dir(main) and callable(main.customer_success_balancing)

def test_scenario_one():
    css = [
        {'id': 1, 'score': 60},
        {'id': 2, 'score': 20},
        {'id': 3, 'score': 95},
        {'id': 4, 'score': 75}
    ]

    customers = [
        {'id': 1, 'score': 90},
        {'id': 2, 'score': 20},
        {'id': 3, 'score': 70},
        {'id': 4, 'score': 40},
        {'id': 5, 'score': 60},
        {'id': 6, 'score': 10}
    ]
    css_away = [2, 4]
    customer_balancing = main.customer_success_balancing(css, customers, css_away)
    assert customer_balancing == 1