"""
This module contains DuckDuckGoImageSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.search import DuckDuckGoSearchPage


class DuckDuckGoImageSearch(DuckDuckGoSearchPage):
    # Locators: (Add them as Class variables --> all letters as uppercase)
    IMAGES_TAB = (By.CSS_SELECTOR, 'a[data-testid="tab-label-images"]')
    IMAGE_SIZE_DROPDOWN = (By.CLASS_NAME, 'dropdown--size')
    IMAGE_SIZE_MEDIUM = (By.CSS_SELECTOR, 'a[data-value="Medium"]')

    # Constructor:
    def __init__(self, browser, get_url):
        # Call the __init__ of parent:
        super().__init__(browser, get_url)

    # Methods:
    def click_on_item(self, locator):
        tab = self.browser.find_element(*locator)
        tab.click()

    def get_html_css_class_list(self, locator):
        # Method should take in the selector and just return the class_list
        html_element = self.browser.find_element(*locator)
        return html_element.get_attribute("class")

    # TODO:

    # TODO: use BDD words before the method names:
    # TODO: when_change_image_size
    def change_image_size(self):
        # Change the value inside "All sizes" to "Medium"
        image_size_dropdown = self.browser.find_element(*self.IMAGE_SIZE_DROPDOWN)
        image_size_dropdown.click()
        image_size_medium = self.browser.find_element(*self.IMAGE_SIZE_MEDIUM)
        image_size_medium.click()

    # Get all child items under a dropdown:
    def get_all_child_items_in_dropdown(self):
        # div.modal--dropdown--color a.modal__list__link
        dropdown_list = self.browser.find_elements(By.CSS_SELECTOR, 'div.modal--dropdown--color a.modal__list__link')
        for item in dropdown_list:
            print(item)

