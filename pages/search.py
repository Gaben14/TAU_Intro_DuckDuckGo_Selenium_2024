"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver


class DuckDuckGoSearchPage:
    # URL - Class variable
    URL = 'https://www.duckduckgo.com'

    # Locators: (Add them as Class variables --> all letters as uppercase)
    SEARCH_INPUT = (By.ID, 'searchbox_input')

    # Constructor:
    def __init__(self, browser: WebDriver):
        # assigning the browser fixture to self
        self.browser = browser

    def load(self):
        # for using class variables, we need to use self. --> self.URL
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
