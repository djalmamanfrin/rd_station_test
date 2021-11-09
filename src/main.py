

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
    css_available = filter_css_away_and_sort_by_score_asc(css, css_away)

    overloaded_cs = []
    start_score = 0
    for cs in css_available:
        cs_balanced = balanced_by_score(cs, customers, start_score)
        if balanced_by_score is None:
            continue

        customers_ids = list(map(lambda customer: customer['id'], cs_balanced))
        overloaded_cs.append({
            'cs_id': cs['id'],
            'customer_count': len(customers_ids)
        })
        start_score = cs['score']

    overloaded_cs.sort(key=lambda cs: cs['customer_count'], reverse=True)
    first_overloaded_cs = overloaded_cs[0]
    second_overloaded_cs = overloaded_cs[1]
    overloaded_cs_id = 0
    if first_overloaded_cs['customer_count'] != second_overloaded_cs['customer_count']:
        overloaded_cs_id = first_overloaded_cs['cs_id']
    return overloaded_cs_id

def map_entities(scores):
    enumerate_score = enumerate(scores, start=1)
    return [{'id': score[0], 'score': score[1]} for score in enumerate_score]


def build_size_entities(size, score):
    return [score] * size

if __name__ == '__main__':
    print_run_tests()
