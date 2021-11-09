# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    return f'Hi, {name}'  # Press Ctrl+F8 to toggle the breakpoint.


def filter_css_away(css, css_away):
    css_available = list(filter(lambda cs: cs['id'] not in css_away, css))
    css_ids = list(map(lambda cs: cs['id'], css_available))
    return css_ids

def balanced_by_score():
    return 0

def customer_success_balancing(css, customers, cs_away):
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
