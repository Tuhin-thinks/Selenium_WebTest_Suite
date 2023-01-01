from typing import Union
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumScraper:
    
    def __init__(self, page_url: str):
        self.page_url = page_url
        
        # initialize the driver
        self.driver = self.init_driver()
    
    @staticmethod
    def init_driver():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver
    
    def open_url(self, url: str):
        self.page_url = url
        self.driver.get(self.page_url)
        
    def test_selenium(self, **kwargs):
        """
        This method tests the selenium driver for the specified css selector.
        Function should be called with the following kwargs:
        :param css_selector: str
        :return:
        """
        check_with_css_selector = kwargs.get('check_with_css', False)
        check_with_xpath = kwargs.get('check_with_xpath', False)
        check_with_id = kwargs.get('check_with_id', False)
        
        css_selector = kwargs.get('css_selector', None)
        xpath = kwargs.get('xpath', None)
        elem_id = kwargs.get('id', None)
        
        if check_with_css_selector:
            if not css_selector:
                raise ValueError('css_selector is required.')
            element = self.check_with_css_selector(css_selector)
            return element
        
        elif check_with_xpath:
            if not xpath:
                raise ValueError('xpath is required.')
            element = self.check_with_xpath(xpath)
            return element
        
        elif check_with_id:
            if not elem_id:
                raise ValueError('id is required.')
            element = self.check_with_id(elem_id)
            return element
    
    def click_on(self, element_selector: Union[str, WebElement]):
        """
        This method clicks on the specified element.
        
        :param element_selector: Can be a css selector or WebElement.
        :return: None
        """
        if isinstance(element_selector, str):
            element = self.check_with_css_selector(element_selector)
        else:
            element = element_selector
        element.click()
        
    def press_key(self, key_str: str):
        """
        This method emulates pressing a button on the keyboard.
        
        :param key_str: The button to press.
        :return: None
        """
        if key_str.lower() == 'enter':
            webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        elif key_str.lower() == 'esc':
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        elif key_str.lower() == 'tab':
            webdriver.ActionChains(self.driver).send_keys(Keys.TAB).perform()
        elif key_str.lower() == 'space':
            webdriver.ActionChains(self.driver).send_keys(Keys.SPACE).perform()
            
    def enter_text(self, text: str):
        """
        This method enters the specified text.
        
        :param text: The text to enter.
        :return: None
        """
        webdriver.ActionChains(self.driver).send_keys(text).perform()
        
    def write_text(self, text: str):
        """
        This method writes the specified text.
        
        :param text: The text to write.
        :return: None
        """
        webdriver.ActionChains(self.driver).send_keys(text).perform()
        
    def find_element(self, selector: str, selector_type: str):
        """
        This method finds the specified element.
        
        :param selector_type: The type of selector to use.
        :param selector: The selector to use.
        :return: None
        """
        if selector_type == 'css':
            return self.check_with_css_selector(selector)
        
        elif selector_type == 'xpath':
            return self.check_with_xpath(selector)
        
        elif selector_type == 'id':
            return self.check_with_id(selector)
        
    def get_all_elemText(self, selector, selector_type) -> list:
        """
        This method gets all the text from the specified element.
        
        :param selector: The selector to use.
        :param selector_type: The type of selector to use.
        :return: None
        """
        if selector_type == 'css':
            selector_type = By.CSS_SELECTOR
        elif selector_type == 'xpath':
            selector_type = By.XPATH
        elif selector_type == 'id':
            selector_type = By.ID
        else:
            raise ValueError('Invalid selector type.')
            
        elements = self.driver.find_elements(selector_type, selector)
        text = []
        for element in elements:
            text.append(element.text)
        return text
    
    def get_elemText(self, selector, selector_type) -> str:
        """
        This method gets the text from the specified element.
        
        :param selector: The selector to use.
        :param selector_type: The type of selector to use.
        :return: None
        """
        if selector_type == 'css':
            selector_type = By.CSS_SELECTOR
        elif selector_type == 'xpath':
            selector_type = By.XPATH
        elif selector_type == 'id':
            selector_type = By.ID
        else:
            raise ValueError('Invalid selector type.')
            
        element = self.driver.find_element(selector_type, selector)
        return element.text
    
    def check_with_css_selector(self, css_selector: str):
        """
        This method checks if the driver can access the specified css selector.
        
        :return: None
        """
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
            return element
        except Exception as e:
            print(e)
            return None
    
    def check_with_xpath(self, xpath: str):
        """
        This method checks if the driver can access the specified xpath.
        
        :return: None
        """
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            return element
        except Exception as e:
            print(e)
            return None
    
    def check_with_id(self, elem_id: str):
        """
        This method checks if the driver can access the specified id.
        
        :return: None
        """
        try:
            element = self.driver.find_element(By.ID, elem_id)
            return element
        except Exception as e:
            print(e)
            return None
    
    def close_driver(self):
        """
        This method closes the driver.
        
        :return: None
        """
        self.driver.close()
