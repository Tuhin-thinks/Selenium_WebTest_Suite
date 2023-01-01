# writing a suite to test any web url for its accessibility in scraping.
from typing import Union
from pathlib import Path
import json
from selenium_suite.scraper_selenium import SeleniumScraper
from Suite_IO import get_selector, menu


class AutoTest:
    """
    This class is the auto test suite for the selenium scraper.
                        or,
    To record the user's actions and create a test suite.
    """
    
    def __init__(self, page_url: str, test_suite_file: Union[str, Path] = None):
        self.page_url = page_url
        
        # initialize the test suite
        self.test_suite = []
        self.temp_test_suite = []
        
        # initialize the test suite file
        self.test_suite_file = test_suite_file
        if isinstance(test_suite_file, str):
            self.test_suite_file = Path(test_suite_file)
        
        if self.test_suite_file.exists():
            self.test_suite_file.unlink()  # delete the file if it exists
        
        # define aliases
        self.save = self.exit  # alias for exit method.
    
    def record_step(self, step: dict):
        """
        This method records the step in the test suite.
        
        :param step: dict
        :return: None
        """
        self.test_suite.append(step)
    
    def record_temp_step(self, step):
        self.temp_test_suite.append(step)
    
    def write_test_suite(self):
        """
        This method writes the test suite to a file.
        
        :return: None
        """
        if not self.test_suite_file:
            raise ValueError('test_suite_file is required.')
        
        # write the test suite algorithm to the file
        with open(self.test_suite_file, 'w') as self.test_suite_file:
            json.dump(self.test_suite, self.test_suite_file, indent=4)
        
        print('Test suite written to file.')  # Todo: change this to log writing instead of printing.
    
    def click_on(self, element_selector, selector_type):
        self.record_step({"click_on": {"selector": element_selector, "selector_type": selector_type}})
    
    def find_element(self, selector, selector_type):
        self.record_temp_step({"find_element": {"selector": selector, "selector_type": selector_type}})
    
    def open_url(self, url):
        self.record_step({"open_url": {"url": url}})
    
    def press_key(self, key):
        if key not in ('enter', 'tab', 'esc', 'escape', 'backspace', 'space'):
            self.record_step({"enter_text": {"text": key}})
        else:
            self.record_step({"press_key": {"key": key}})
    
    def get_all_elemText(self, selector=None, selector_type=None):
        # For this step, either we need to have a temp step to find the element, or
        # the find element step should be a part of the get_all_elemText step.
        
        if not (selector or selector_type):  # if both are None
            # check if the temp test suite is empty
            if not self.temp_test_suite:
                raise ValueError('No element found.')
            
            # get the element (only the last element to be used)
            element = self.temp_test_suite[-1]['find_element']
            selector_type, selector = element['selector_type'], element['selector']
        
            # clear the temp test suite
            self.temp_test_suite.clear()
        # --------------------------------------------------
        # record the step
        self.record_step({"get_all_elemText": {"selector": selector, "selector_type": selector_type}})
    
    def get_elemText(self, selector=None, selector_type=None):
        # For this step, either we need to have a temp step to find the element, or
        # the find element step should be a part of the get_elemText step.

        if not (selector or selector_type):  # if both are None
            # check if the temp test suite is empty
            if not self.temp_test_suite:
                raise ValueError('No element found.')
    
            # get the element (only the last element to be used)
            element = self.temp_test_suite[-1]['find_element']
            selector_type, selector = element['selector_type'], element['selector']
    
            # clear the temp test suite
            self.temp_test_suite.clear()
        # --------------------------------------------------
        # record the step
        self.record_step({"get_elemText": {"selector": selector, "selector_type": selector_type}})
    
    def get_elemAttr(self, attr, selector=None, selector_type=None):
        # For this step, either we need to have a temp step to find the element, or
        # the find element step should be a part of the get_elemAttr step.
        
        if not (selector or selector_type):  # if both are None
            # check if the temp test suite is empty
            if not self.temp_test_suite:
                raise ValueError('No element found.')
            
            # get the element (only the last element to be used)
            element = self.temp_test_suite[-1]['find_element']
            selector_type, selector = element['selector_type'], element['selector']
            
            # clear the temp test suite
            self.temp_test_suite.clear()
        # --------------------------------------------------
        
        # record the step
        self.record_step({"get_elemAttr": {"selector": selector, "selector_type": selector_type, "attr": attr}})
    
    def get_elemHTML(self, selector=None, selector_type=None):
        # For this step, either we need to have a temp step to find the element, or
        # the find element step should be a part of the get_elemHTML step.
        
        if not (selector or selector_type):  # if both are None
            # check if the temp test suite is empty
            if not self.temp_test_suite:
                raise ValueError('No element found.')
            
            # get the element (only the last element to be used)
            element = self.temp_test_suite[-1]['find_element']
            selector_type, selector = element['selector_type'], element['selector']
            
            # clear the temp test suite
            self.temp_test_suite.clear()
        # --------------------------------------------------
        # record the step
        self.record_step({"get_elemHTML": {"selector": selector, "selector_type": selector_type}})
    
    def exit(self):
        self.record_step({"exit": {}})
        self.write_test_suite()  # write the test suite to the file.


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
    if choice in ('7', '8', '9', '10'):
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
        return "get_elemAttr", test_or_record, selector, selector_type
    
    elif choice == '10':
        return "get_elemHTML", test_or_record, selector, selector_type


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
            selenium_test_suite.get_all_elemText(selector, selector_type)
            if test_or_record == 'record':
                test_suite_recorder.get_all_elemText(selector, selector_type)
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
