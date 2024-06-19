"""
These tests (test cases) cover DuckDuckGo searches.
"""
import pytest
from selenium.webdriver import Keys

from pages.result import DuckDuckGoSearchResult
from pages.search import DuckDuckGoSearchPage
from pages.search_validation import DuckDuckGoSearchValidation
from utils.locators_search import SearchPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestSearch:
    """
    Test Case:

    1. Open the browser and the https://duckduckgo.com page
        - Assert if the page has been opened successfully - HTTP 200
    2. Find the search-bar. Enter the phrase.
        - Assert if there are any search results
        - Assert if the page title contains the search phrase
    4. Change the value inside "Regions" to a random value
        - Assert if value has been changed to the random value
    5. Change the "Settings" inside search
        - Assert if the values have been changed after clicking on them
    6. Open a random search result
        - Assert if the search result contains the Phrase
    7. Check if the autocomplete search result suggestions contain the Phrase
    """
    # Class Variable
    PHRASE = "panda"

    # @pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
    def test_basic_duckduckgo_search(self, browser):  # phrase
        search_page = DuckDuckGoSearchPage(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)
        result_page = DuckDuckGoSearchResult(browser)

        # WHEN the user searches for "panda"
        search_page.when_user_searches(self.PHRASE)

        # THEN Assert that the search result query = "panda"
        search_page_validation.then_assert_variable_is_equal_to_variable(
            self.PHRASE, result_page.then_get_search_input_value())

        # AND the search result links pertain (relates) to "panda"
        titles = result_page.then_get_result_link_titles()
        matches = [t for t in titles if self.PHRASE.lower() in t.lower()]

        # THEN Assert search result is greater than 0
        search_page_validation.then_assert_search_result_is_greater_as_0(len(matches))

        # THEN assert the search result title contains "panda"
        result_page_title = result_page.then_get_title().lower()
        search_page_validation.then_assert_value_in_data_type(self.PHRASE, result_page_title)

        # AND click on more results:
        result_page.when_user_clicks_on_more_results()

    def test_duckduckgo_regions_settings(self, browser):
        search_page = DuckDuckGoSearchPage(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)
        search_page.when_user_searches(self.PHRASE)

        # Click on "All regions" dropdown
        regions_filter_dropdown = WebDriverWait(browser, 25).until(
            EC.visibility_of_element_located(SearchPageLocators.REGIONS_CURRENT_LINK)
        )
        regions_filter_dropdown.click()

        # Get a random regions Text
        regions_list = browser.find_elements(*SearchPageLocators.REGIONS_DROPDOWN_LINK)

        # Starting from 1 because the "All Regions" is the first one.
        rd_regions_index = search_page.then_get_rnd_number(1, len(regions_list))
        # rd_regions_innerHTML = regions_list[rd_regions_index].get_attribute("innerHTML")
        rd_regions_text = regions_list[rd_regions_index].get_attribute("text")

        # Enter the random regions value in the region filter input field
        regions_filter_input = browser.find_element(*SearchPageLocators.REGIONS_FILTER_INPUT)
        regions_filter_input.clear()
        regions_filter_input.send_keys(rd_regions_text)

        # Click on the Result input field
        regions_filter_result = browser.find_element(*SearchPageLocators.REGIONS_FILTER_INPUT_RESULT)
        regions_filter_result.click()

        # THEN Assert that the Region Toggle Div aria-checked has the value True
        search_page_validation.then_assert_value_in_html_element(
            SearchPageLocators.REGIONS_DROPDOWN_SWITCH, 'class', 'is-on')

        # THEN Assert that the text of REGIONS_DROPDOWN_LINK is the same
        # as for the random value.
        search_page_validation.then_assert_value_is_equal_to_html_element(
            SearchPageLocators.REGIONS_CURRENT_LINK, "text", rd_regions_text)

    def test_duckduckgo_search_settings(self, browser):
        search_page = DuckDuckGoSearchPage(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        search_page.when_user_searches(self.PHRASE)

        # Click on the "Settings" button
        search_page.when_user_clicks_on_item(SearchPageLocators.SETTINGS_LINK)

        # Change to Dark Mode, by clicking on the div[data-theme-id="d"]
        search_page.when_user_clicks_on_item(SearchPageLocators.DARK_MODE)

        # Assert that the Dark Mode label has the is-checked class
        search_page_validation.then_assert_html_element_has_is_checked_cls(
            SearchPageLocators.DARK_MODE_LABEL)

        # Click on the Font Size dropdown
        search_page.when_user_clicks_on_item(SearchPageLocators.FONT_SIZE_DROPDOWN)
        # Change to a random font size
        font_size_childs_options = browser.find_elements(*SearchPageLocators.FONT_SIZE_DROPDOWN_OPTIONS)
        rd_font_size_index = search_page.then_get_rnd_number(0, len(font_size_childs_options))
        font_size_childs_options[rd_font_size_index].click()

        # Click on the Font dropdown
        search_page.when_user_clicks_on_item(SearchPageLocators.FONT_FAMILY_DROPDOWN)
        # Change to a random Font
        font_family_childs_options = browser.find_elements(*SearchPageLocators.FONT_FAMILY_DROPDOWN_OPTIONS)
        rd_font_family_index = search_page.then_get_rnd_number(0, len(font_family_childs_options))
        font_family_childs_options[rd_font_family_index].click()

        # Click on the Display Language dropdown
        search_page.when_user_clicks_on_item(SearchPageLocators.LANGUAGE_DROPDOWN)

        # Change the value to "Hungarian"
        search_page.when_user_clicks_on_item(SearchPageLocators.LANGUAGE_HUNGARIAN)

        # Click again on the Settings:
        search_page.when_user_clicks_on_item(SearchPageLocators.SETTINGS_LINK)

        # Click on the Infinite Scroll flipper
        search_page.when_user_clicks_on_item(SearchPageLocators.INFINITY_SCROLL_TOGGLE)

        # Assert that the grandparent div of label[for="setting_kav"] has the "is-checked" class
        search_page_validation.then_assert_html_element_has_is_checked_cls(
            SearchPageLocators.INFINITY_SCROLL_GPARENT_DIV)

        # Click on the 'Open Links in a New Tab' flipper, it should be turned on
        search_page.when_user_clicks_on_item(SearchPageLocators.OPEN_LINKS_TOGGLE)
        # open_new_gparent_cls_list = search_page.then_get_attribute_for_html_element(
        #    SearchPageLocators.OPEN_LINKS_GPARENT_DIV, "class")

        # Assert that the OPEN_LINKS_GPARENT_DIV of
        # 'Open Links in a New Tab' has the 'is-checked class'
        search_page_validation.then_assert_html_element_has_is_checked_cls(
            SearchPageLocators.OPEN_LINKS_GPARENT_DIV)

        # Click on the Reset buttons
        search_page.when_user_clicks_on_item(SearchPageLocators.APPEARANCE_RESET_LINK)
        search_page.when_user_clicks_on_item(SearchPageLocators.GENERAL_RESET_LINK)

        # Again click on the Settings
        search_page.when_user_clicks_on_item(SearchPageLocators.SETTINGS_LINK)

        # Assert that Light Mode Label has the "is-checked" class
        search_page_validation.then_assert_html_element_has_is_checked_cls(
            SearchPageLocators.LIGHT_MODE_LABEL)

        # Assert that the grandparent div of Infinity Scroll
        # does not have the "is-checked" class
        search_page_validation.then_assert_data_type_does_not_have_is_checked(
            SearchPageLocators.INFINITY_SCROLL_GPARENT_DIV)

        # Assert that grandparent of Open New Tab
        # does not have the is-checked class
        search_page_validation.then_assert_data_type_does_not_have_is_checked(
            SearchPageLocators.OPEN_LINKS_GPARENT_DIV)

    def test_random_article(self, browser):
        search_page = DuckDuckGoSearchPage(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)
        result_page = DuckDuckGoSearchResult(browser)

        # WHEN the user searches for "phrase"
        search_page.when_user_searches(self.PHRASE)

        # AND: Click on search result
        search_page.when_user_clicks_on_rnd_search_result()

        # THEN assert search result contains 'Phrase' in title
        # assert self.PHRASE in result_page.then_get_title().lower()
        result_page_title = result_page.then_get_title().lower()
        # AssertSearch.assert_value_in_data_type(self.PHRASE, result_page_title)
        search_page_validation.then_assert_value_in_data_type(self.PHRASE, result_page_title)

    def test_autocomplete_search(self, browser):
        # GIVEN the DuckDuckGo home page is displayed
        search_page = DuckDuckGoSearchPage(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        # WHEN the user searches for "panda"
        autocomplete_result_list = search_page.when_user_enters_phrase_in_search_autocomplete(self.PHRASE)
        # THEN Assert if the autocomplete results contain the 'phrase'
        for auto_c_item in autocomplete_result_list:
            # AssertSearch.assert_value_in_data_type(self.PHRASE, auto_c_item.text)
            search_page_validation.then_assert_value_in_data_type(self.PHRASE, auto_c_item.text)

        # AND Randomly click on one of the autocomplete suggestion results
        search_page.then_click_on_autocomplete_result(autocomplete_result_list)
