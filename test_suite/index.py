from pathlib import Path
from typing import Union
import json


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
