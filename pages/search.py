"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from selenium import common
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logs.log_configuration import log_details

from utils.locators_search import SearchPageLocators

import random


class DuckDuckGoSearchPage:

    # Constructor:
    def __init__(self, browser: WebDriver):
        # assigning the browser fixture to self
        self.browser = browser

    def validate_if_locator_exists(self, locator):
        try:
            return self.browser.find_element(*locator)
        except common.NoSuchElementException as e:
            log_details().critical(e.msg)
            raise common.NoSuchElementException

    def validate_if_locators_exists(self, locators):
        try:
            return self.browser.find_elements(*locators)
        except common.NoSuchElementException as e:
            log_details().critical(e.msg)
            raise common.NoSuchElementException


    def when_user_searches(self, phrase):
        # search_input = self.browser.find_element(*SearchPageLocators.SEARCH_INPUT)
        search_input = self.validate_if_locator_exists(SearchPageLocators.SEARCH_INPUT)
        search_input.clear()

        search_input.send_keys(phrase)
        search_button = self.validate_if_locator_exists(SearchPageLocators.SEARCH_BUTTON)
        search_button.click()

    def when_user_clicks_on_rnd_search_result(self):
        # Click on a random search result, from 1 to 10
        # article#r1-0 (Here the 2nd number can be 0 to 9
        rnd_article = self.validate_if_locator_exists(SearchPageLocators.RANDOM_ARTICLE)
        # After you have the random Article,
        # click inside the <a> with data-testid="result-title-a
        rnd_article.click()

    def when_user_clicks_on_item(self, locator):
        html_element = self.validate_if_locator_exists(locator)
        html_element.click()

    def when_user_enters_phrase_in_search_autocomplete(self, phrase):
        # Click in the search_input selector and enter a text to search
        search_input = self.validate_if_locator_exists(SearchPageLocators.SEARCH_INPUT)
        search_input.send_keys(phrase)
        # Get all the autocomplete suggestions inside a list
        # Wait explicitly until the autocomplete is visible
        autocomplete_container = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(SearchPageLocators.AUTOCOMPLETE_CONTAINER)
        )

        autocomplete_suggestions_li = self.validate_if_locators_exists(
            SearchPageLocators.AUTOCOMPLETE_SUGGESTIONS_LI)

        return autocomplete_suggestions_li

    def then_click_on_autocomplete_result(self, autocomplete_list):
        # Randomly click on one of the autocomplete suggestion results
        autocomplete_list[SearchPageLocators.rnd_num].click()

    def then_get_child_link_of_dropdown_menu(self, dropdown_name):
        """
        For some reason the div[class=""] CSS selector is not working here in Selenium
        (By.CSS_SELECTOR, 'div[class="dropdown  dropdown--license is-active"] > a')
        I had to use this solution:
        dropdown = self.browser.find_element(By.CSS_SELECTOR, f'div.dropdown--{dropdown_name}.is-active')
        """
        dropdown_child_a = self.validate_if_locator_exists(By.CSS_SELECTOR, f'div.dropdown--{dropdown_name}.is-active > a')
        return dropdown_child_a

    def then_get_rnd_number(self, num_1, num_2):
        return random.randint(num_1, num_2 - 1)

    def then_get_attribute_for_html_element(self, locator, attribute):
        html_element = self.validate_if_locator_exists(locator)
        return html_element.get_attribute(attribute)
