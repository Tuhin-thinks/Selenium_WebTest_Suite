import json
import os
from . import get_selector
from global_settings import PRINT_FINDINGS


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


class SaveMenu:
    """
    This class is the menu to provide option for save the test results
    """
    
    def ask_save(self):
        """
        This function asks the user if they want to save the test results.
        :return: bool
        """
        save = input('Do you want to save the test results? (y/n): ')
        if save.lower() == 'y':
            return True, self.ask_save_path()
        elif save.lower() == 'n':
            return False, None
        else:
            print('Invalid input. Please try again.')
            return self.ask_save()
        
    @staticmethod
    def ask_save_path():
        """
        This function asks the user for the save path.
        :return: str
        """
        save_path = input('Enter the save path: ')
        if not save_path:
            print('Invalid input. Please try again.')
            return SaveMenu.ask_save_path()
        elif os.path.exists(save_path):
            print('Invalid input. File already exists.')
            return SaveMenu.ask_save_path()
        else:
            return save_path
        
    @staticmethod
    def save_file(test_results, save_path):
        """
        This function saves the test results to a file.
        :param test_results: list
        :param save_path: str
        :return:
        """
        with open(save_path, 'w') as f:
            json.dump(test_results, f, indent=4)
        
        if PRINT_FINDINGS:
            print(f'Test results saved to file: {save_path}')
