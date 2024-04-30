"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DuckDuckGoSearchPage:
    # Locators: (Add them as Class variables --> all letters as uppercase)
    SEARCH_INPUT = (By.ID, 'searchbox_input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[aria-label="Search"]')
    RESULT_TITLE = (By.CSS_SELECTOR, '[data-testid="result-title-a"]')
    rnd_num = random.randint(0, 9)
    RANDOM_ARTICLE = (By.CSS_SELECTOR, f"#r1-{rnd_num} a[data-testid='result-title-a']")
    AUTOCOMPLETE_CONTAINER = (By.ID, 'listbox--searchbox_homepage')
    AUTOCOMPLETE_SUGGESTIONS_LI = (By.CLASS_NAME, 'searchbox_suggestion__csrUQ')

    # Constructor:
    def __init__(self, browser: WebDriver, get_url):
        # assigning the browser fixture to self
        self.browser = browser
        self.get_url = get_url

    def load(self):
        # for using class variables, we need to use self. --> self.URL
        self.browser.get(self.get_url)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.clear()
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

    def search_autocomplete(self, phrase):
        # Click in the search_input selector and enter a text to search
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        # Get all the autocomplete suggestions inside a list
        # Wait explicitly until the autocomplete is visible
        autocomplete_container = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.AUTOCOMPLETE_CONTAINER)
        )
        autocomplete_suggestions_li = self.browser.find_elements(*self.AUTOCOMPLETE_SUGGESTIONS_LI)

        return autocomplete_suggestions_li

    def click_on_autocomplete_result(self, autocomplete_list):
        # Randomly click on one of the autocomplete suggestion results
        autocomplete_list[self.rnd_num].click()
