"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
import random

class DuckDuckGoSearchPage:
    # URL - Class variable
    URL = 'https://www.duckduckgo.com'

    # Locators: (Add them as Class variables --> all letters as uppercase)
    SEARCH_INPUT = (By.ID, 'searchbox_input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[aria-label="Search"]')
    RESULT_TITLE = (By.CSS_SELECTOR, '[data-testid="result-title-a"]')
    rnd_num = random.randint(0, 9)
    RANDOM_ARTICLE = (By.CSS_SELECTOR, f"#r1-{rnd_num} a[data-testid='result-title-a']")

    # Constructor:
    def __init__(self, browser: WebDriver):
        # assigning the browser fixture to self
        self.browser = browser

    def load(self):
        # for using class variables, we need to use self. --> self.URL
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        # search_input.send_keys(phrase + Keys.RETURN)
        search_input.send_keys(phrase)
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def click_on_search_result(self):
        # Click on a random search result, from 1 to 10
        # article#r1-0 (Here the 2nd number can be 0 to 9
        rnd_article = self.browser.find_element(*self.RANDOM_ARTICLE)
        # After you have the random Article,
        # click inside the <a> with data-testid="result-title-a
        rnd_article.click()

