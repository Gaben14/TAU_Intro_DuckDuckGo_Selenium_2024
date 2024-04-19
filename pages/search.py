"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from selenium.webdriver.common.by import By


class DuckDuckGoSearchPage:

    # Locators: (Add them as Class variables --> all letters as uppercase)
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    # Constructor:
    def __init__(self, browser):
        # assigning the browser fixture to self
        self.browser = browser

    def load(self):
        # TODO
        pass

    def search(self, phrase):
        # TODO
        pass