import pytest
from src import main

def test_assert_print_run_tests():
    assert 'Hi, run tests' == main.print_run_tests()


def test_filter_css_away_method_exists_and_is_callable():
    assert "filter_css_away_and_sort_by_score_asc" in dir(main) and callable(main.filter_css_away_and_sort_by_score_asc)


def test_filter_css_away():
    css = [
        {'id': 1, 'score': 60},
        {'id': 2, 'score': 20},
        {'id': 3, 'score': 95},
        {'id': 4, 'score': 75}
    ]
    css_away = [2, 4]
    css_available = main.filter_css_away_and_sort_by_score_asc(css, css_away)
    css_available_ids = [cs_available['id'] for cs_available in css_available]
    assert css_available_ids == [1, 3]


def test_before_filter_css_away_must_be_sorted_by_score_asc():
    css = [
        {'id': 1, 'score': 60},
        {'id': 2, 'score': 20},
        {'id': 3, 'score': 95},
        {'id': 4, 'score': 75}
    ]
    css_away = [3, 4]
    css_available = main.filter_css_away_and_sort_by_score_asc(css, css_away)
    css_available_ids = [cs_available['id'] for cs_available in css_available]
    assert css_available_ids == [2, 1]


def test_balanced_by_score_method_exists_and_is_callable():
    assert "balanced_by_score" in dir(main) and callable(main.balanced_by_score)


def test_balanced_by_score():
    cs = {'id': 1, 'score': 60}
    customers = [
        {'id': 1, 'score': 90},
        {'id': 2, 'score': 20},
        {'id': 3, 'score': 70},
        {'id': 4, 'score': 40},
        {'id': 5, 'score': 60},
        {'id': 6, 'score': 10}
    ]
    start_score = 0
    balanced_by_score = main.balanced_by_score(cs, customers, start_score)
    assert len(balanced_by_score) == 4


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