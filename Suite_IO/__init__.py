def get_selector(selector_type='') -> tuple:
    
    # get the selector type to test, enter id:#element_id, xpath://element_xpath, css:#element_css
    selector_string = input(f'Enter the {selector_type or "selector type"}.\n'
                            '' if selector_type else 'Enter id:#element_id, xpath://element_xpath, css:#element_css\n'
                            'Enter the selector: ')
    if not selector_string:
        raise ValueError('selector is required.')
    
    # check if css selector is already provided in the argument
    if selector_type in ('css', 'id', 'xpath'):
        selector = selector_string
        return selector, selector_type
    
    # if not, check if the selector is provided in the selector string
    try:
        selector_type = selector_string.split(':')[0]
        selector = selector_string.split(':')[1]
    except IndexError:
        raise ValueError('selector is required.\n'
                         'Make sure to enter the selector type and the selector separated by a colon.')
    return selector, selector_type
