"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import locators_search


class DuckDuckGoSearchPage:

    # Constructor:
    def __init__(self, browser: WebDriver, get_url):
        # assigning the browser fixture to self
        self.browser = browser
        self.get_url = get_url

    def load(self):
        # for using class variables, we need to use self. --> self.URL
        self.browser.get(self.get_url)

    def search(self, phrase):
        search_input = self.browser.find_element(*locators_search.SEARCH_INPUT)
        search_input.clear()

        search_input.send_keys(phrase)
        search_button = self.browser.find_element(*locators_search.SEARCH_BUTTON)
        search_button.click()

    def click_on_rnd_search_result(self):
        # Click on a random search result, from 1 to 10
        # article#r1-0 (Here the 2nd number can be 0 to 9
        rnd_article = self.browser.find_element(*locators_search.RANDOM_ARTICLE)
        # After you have the random Article,
        # click inside the <a> with data-testid="result-title-a
        rnd_article.click()

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

    def search_autocomplete(self, phrase):
        # Click in the search_input selector and enter a text to search
        search_input = self.browser.find_element(*locators_search.SEARCH_INPUT)
        search_input.send_keys(phrase)
        # Get all the autocomplete suggestions inside a list
        # Wait explicitly until the autocomplete is visible
        autocomplete_container = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(locators_search.AUTOCOMPLETE_CONTAINER)
        )
        autocomplete_suggestions_li = self.browser.find_elements(*locators_search.AUTOCOMPLETE_SUGGESTIONS_LI)

        return autocomplete_suggestions_li

    def click_on_autocomplete_result(self, autocomplete_list):
        # Randomly click on one of the autocomplete suggestion results
        autocomplete_list[locators_search.rnd_num].click()


