from . import get_selector


def find_element_menu():
    """
    This function displays the find element menu.
    Returns the selector and the selector type.
    
    :return: tuple
    """
    menu_display_str = """\
Please select an option:
    1. Find element by css selector.
    2. Find element by xpath.
    3. Find element by id.

Enter your choice:"""
    
    # get the user's choice
    choice = input(menu_display_str)
    selector_choice_mapping = {
        '1': 'css',
        '2': 'xpath',
        '3': 'id'
    }
    # check the user's choice
    if choice in selector_choice_mapping:
        selector_type = selector_choice_mapping[choice]
        selector, selector_type = get_selector(selector_type)
        
        return selector, selector_type
