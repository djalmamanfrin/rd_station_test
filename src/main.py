

def print_run_tests():
    return 'Hi, run tests'


def filter_css_away_and_sort_by_score_asc(css, css_away):
    css_filtered = list(filter(lambda cs: cs['id'] not in css_away, css))
    css_filtered.sort(key=lambda cs: cs['score'])
    return css_filtered

def balanced_by_score(cs, customers, start_score):
    css = [customer for customer in customers if start_score < customer['score'] <= cs['score']]
    return  css

def customer_success_balancing(css, customers, css_away):
    return 0


if __name__ == '__main__':
    print_run_tests()
