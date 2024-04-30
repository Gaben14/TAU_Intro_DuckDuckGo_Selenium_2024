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
    IMAGES_TAB = (By.CSS_SELECTOR, '[data-testid="tab-label-images"]')
    IMAGE_SIZE_DROPDOWN = (By.CLASS_NAME, 'dropdown--size')
    IMAGE_SIZE_MEDIUM = (By.CSS_SELECTOR, 'a[data-value="Medium"]')

    # Constructor:
    def __init__(self, browser, get_url):
        # Call the __init__ of parent:
        super().__init__(browser, get_url)

    # Methods:

    def click_on_images_tab(self):
        images_tab = self.browser.find_element(*self.IMAGES_TAB)
        images_tab.click()

    def html_css_class_list(self, locator):
        # Method should take in the selector and just return the class_list
        html_element = self.browser.find_element(*locator)
        return html_element.get_attribute("class")

    def change_image_size(self):
        # Change the value inside "All sizes" to "Medium"
        image_size_dropdown = self.browser.find_element(*self.IMAGE_SIZE_DROPDOWN)
        image_size_dropdown.click()
        image_size_medium = self.browser.find_element(*self.IMAGE_SIZE_MEDIUM)
        image_size_medium.click()


