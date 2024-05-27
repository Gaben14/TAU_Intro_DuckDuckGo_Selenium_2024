"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# to use the Intellisense for selenium, we need to import WebDriver and assign it
# to browser in the constructor


class DuckDuckGoSearchResult:
    # Locators:
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    MORE_RESULTS = (By.ID, "more-results")

    # Constructor - Initializer
    def __init__(self, browser: WebDriver):
        self.browser = browser

    # Interaction Methods

    def when_user_clicks_on_more_results(self):
        more_results = self.browser.find_element(*self.MORE_RESULTS)
        more_results.click()

    def then_get_result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def then_get_search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def then_get_title(self):
        return self.browser.title

