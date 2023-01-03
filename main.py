# writing a suite to test any web url for its accessibility in scraping.
from selenium_suite.scraper_selenium import SeleniumScraper
from Suite_IO import get_selector, menu
from test_suite import AutoTest


def user_io():
    """
    This function is the menu for the program.
    :return:
    """
    menu_display_str = """\
Welcome to the Selenium Suite.
Please select an option:
    1. Test the selenium suite.
    2. "Click on" menu >>
    3. "Find Element" menu >>
    4. Open the url in the browser.
    5. Press Key.
    6. Exit.
    ----------------------
    7. "Get all element text" menu >>
    8. "Get element text" menu >>
    9. "Get element attribute" menu >>
    10. "Get element HTML" menu >>

Enter your choice:"""
    
    # get the user's choice
    choice = input(menu_display_str)
    
    test_or_record = None
    selector, selector_type = None, None
    if choice in ('7', '8', '9', '10', '11'):
        # ask if user just wants to test it or record it
        test_or_record = input('Do you want to test or record this step? (test/record): ')
        # redirect user to the get_selector() menu
        selector, selector_type = get_selector()
    
    # check the user's choice
    if choice == '1':
        return "test_selenium"
    
    elif choice == '2':
        # get the element to click on
        selector, selector_type = get_selector()
        return "click_on", selector, selector_type
    
    elif choice == '3':
        # redirect to the find element menu
        selector, selector_type = menu.find_element_menu()
        return "find_element", selector, selector_type
    
    elif choice == '4':
        url = input('Enter the url to open: ')
        return "open_url", url
    
    elif choice == '5':
        return "press_key",
    
    elif choice == '6':
        return "exit",
    
    elif choice == '7':
        return "get_all_elemText", test_or_record, selector, selector_type
    
    elif choice == '8':
        return "get_elemText", test_or_record, selector, selector_type
    
    elif choice == '9':
        attribute = input('Enter the attribute to get: ')
        return "get_elemAttr", test_or_record, selector, selector_type, attribute
    
    elif choice == '10':
        return "get_elemHTML", test_or_record, selector, selector_type
    
    elif choice == '11':
        attribute = input('Enter the attribute to get: ')
        return "get_elemAttr", test_or_record, selector, selector_type, attribute


def test_selenium():
    """
    This function tests the selenium suite.
    :return:
    """
    selenium_test_suite = main()
    test_suite_recorder = AutoTest(page_url=selenium_test_suite.page_url,
                                   test_suite_file='test_suite.json')
    while 1:
        # design the test suite
        choice_, *args = user_io()
        
        if choice_ == "test_selenium":
            selenium_test_suite.test_selenium()
        
        elif choice_ == "click_on":
            selector, selector_type = args
            # record the step
            test_suite_recorder.click_on(element_selector=selector, selector_type=selector_type)
            # perform the step
            selenium_test_suite.click_on(selenium_test_suite.find_element(selector, selector_type))
        
        elif choice_ == "press_key":
            key = input('Enter the key to press: ')
            test_suite_recorder.press_key(key)  # record the step
            
            # perform the step
            if key not in ('enter', 'tab', 'esc', 'escape', 'backspace', 'space'):
                selenium_test_suite.enter_text(key)  # enter the text on the focussed element
            else:
                selenium_test_suite.press_key(key)
        
        elif choice_ == "find_element":
            selector, selector_type = args
            # record the step
            test_suite_recorder.find_element(selector, selector_type)
            # perform the step
            element = selenium_test_suite.test_selenium(
                **{f"check_with_{selector_type}": True, f"{selector_type}_selector": selector})
            print(element)
        
        elif choice_ == "open_url":
            url = args[0]
            # record the step
            test_suite_recorder.open_url(url)
            # perform the step
            selenium_test_suite.open_url(url)
        
        elif choice_ == "exit":
            break
        
        elif choice_ == "get_all_elemText":
            test_or_record = args[0]
            selector, selector_type = args[1], args[2]
            results = selenium_test_suite.get_all_elemText(selector, selector_type)
            _save = menu.SaveMenu()
            to_save, save_path = _save.ask_save()
            if to_save:
                _save.save_file(results, save_path)
            if test_or_record == 'record':
                test_suite_recorder.get_all_elemText(selector, selector_type)
        
        elif choice_ == "get_elemText":
            test_or_record = args[0]
            selector, selector_type = args[1], args[2]
            selenium_test_suite.get_elemText(selector, selector_type)
            if test_or_record == 'record':
                test_suite_recorder.get_elemText(selector, selector_type)
        
        elif choice_ == "get_elemAttr":
            test_or_record = args[0]
            selector, selector_type = args[1], args[2]
            attribute = args[3]
            attribute_string = selenium_test_suite.get_elemAttr(selector, selector_type, attribute)
            print(attribute_string)
            if test_or_record == 'record':
                test_suite_recorder.get_elemAttr(selector, selector_type)
                
        elif choice_ == "get_allElemAttr":
            test_or_record = args[0]
            selector, selector_type = args[1], args[2]
            attribute = args[3]
            all_attributes = selenium_test_suite.get_allElemAttr(selector, selector_type, attribute)
            print(all_attributes)
            if test_or_record == 'record':
                test_suite_recorder.get_allElemAttr(selector, selector_type)
                
        elif choice_ == "get_elemHTML":
            test_or_record = args[0]
            selector, selector_type = args[1], args[2]
            selenium_test_suite.get_elemHTML(selector, selector_type)
            if test_or_record == 'record':
                test_suite_recorder.get_elemHTML(selector, selector_type)
        else:
            print('Invalid choice. Please try again.')
        
        print("---------------------------------------------------")
    
    # write the test suite to the file
    test_suite_recorder.save()


def main():
    """
    This function is the main function of the program.
    :return:
    """
    # get the url to test
    url = input('Enter the url to test: ')
    
    # Create a selenium suite instance.
    selenium_suite = SeleniumScraper(page_url=url)
    # Create a selenium driver.
    selenium_suite.init_driver()
    
    selenium_suite.open_url(url)
    
    return selenium_suite


if __name__ == '__main__':
    test_selenium()
