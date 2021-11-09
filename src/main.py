# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    return f'Hi, {name}'  # Press Ctrl+F8 to toggle the breakpoint.


def filter_css_away(css, css_away):
    return list(filter(lambda cs: cs['id'] not in css_away, css))

def balanced_by_score(cs, customers):
    return [customer for customer in customers if customer['score'] <= cs['score']]

def customer_success_balancing(css, customers, css_away):
    css_available = filter_css_away(css, css_away)
    for cs in css_available:
        cs_balanced = balanced_by_score(cs, customers)
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
