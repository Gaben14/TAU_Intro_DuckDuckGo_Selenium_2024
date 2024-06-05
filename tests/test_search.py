"""
These tests (test cases) cover DuckDuckGo searches.
"""
import pytest
from selenium.webdriver import Keys

from pages.result import DuckDuckGoSearchResult
from pages.search import DuckDuckGoSearchPage
from assertions.assert_search import AssertSearch
from utils.locators_search import SearchPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestSearch:
    # Class Variable
    """
    TODO: for later: move Phrase to an enum class, or the URL should already have the
    phrase as a query parameter
    """
    PHRASE = "panda"

    # @pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
    def test_basic_duckduckgo_search(self, browser):  # phrase
        search_page = DuckDuckGoSearchPage(browser)
        result_page = DuckDuckGoSearchResult(browser)

        # WHEN the user searches for "panda"
        search_page.when_user_searches(self.PHRASE)

        # THEN the search result query is "panda"
        # assert self.PHRASE == result_page.then_get_search_input_value()
        AssertSearch.assert_variable_is_equal_to_variable(self.PHRASE, result_page.then_get_search_input_value())

        # AND the search result links pertain (relates) to "panda"
        titles = result_page.then_get_result_link_titles()
        matches = [t for t in titles if self.PHRASE.lower() in t.lower()]

        # assert len(matches) > 0
        AssertSearch.assert_search_result_is_greater_as_0(len(matches))

        # AND the search result title contains "panda"
        # assert self.PHRASE in result_page.then_get_title().lower()
        result_page_title = result_page.then_get_title().lower()
        AssertSearch.assert_value_in_data_type(self.PHRASE, result_page_title)

        # AND click on more results:
        result_page.when_user_clicks_on_more_results()

    def test_duckduckgo_regions_settings(self, browser):
        search_page = DuckDuckGoSearchPage(browser)

        search_page.when_user_searches(self.PHRASE)

        # Click on "All regions" dropdown
        regions_filter_dropdown = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(SearchPageLocators.REGIONS_DROPDOWN_DIV_INACTIVE)
        )
        regions_filter_dropdown.click()

        # Get a random regions Text
        regions_list = browser.find_elements(*SearchPageLocators.REGIONS_LI)

        rd_regions_index = search_page.then_get_rnd_number(0, len(regions_list))
        rd_regions_text = regions_list[rd_regions_index].get_attribute("text")

        # Enter the random regions value in the region filter input field
        regions_filter_input = browser.find_element(*SearchPageLocators.REGIONS_FILTER_INPUT)
        regions_filter_input.clear()
        regions_filter_input.send_keys(rd_regions_text + Keys.RETURN)

        # Assert that the div.dropdown--region has the value 'is-active'
        regions_dd_div_cls_list = search_page.then_get_attribute_for_item(
            SearchPageLocators.REGIONS_DROPDOWN_DIV, 'class')

        AssertSearch.assert_value_in_data_type('is-active', regions_dd_div_cls_list)

        # Assert that the innerHTML of REGIONS_DROPDOWN_LINK innerhtml is the same
        # as for the random value.
        regions_dd_link_text = search_page.then_get_attribute_for_item(
            SearchPageLocators.REGIONS_DROPDOWN_LINK, "text")

        AssertSearch.assert_variable_is_equal_to_variable(rd_regions_text, regions_dd_link_text)

    def test_duckduckgo_search_settings(self, browser):
        search_page = DuckDuckGoSearchPage(browser)

        search_page.when_user_searches(self.PHRASE)

        # Click on the "Settings" button
        search_page.when_user_clicks_on_item(SearchPageLocators.SETTINGS_LINK)

        # Change to Dark Mode, by clicking on the div[data-theme-id="d"]
        search_page.when_user_clicks_on_item(SearchPageLocators.DARK_MODE)
        # Assert that the label has the is-checked class
        dark_mode_label_classes = browser.find_element(*SearchPageLocators.DARK_MODE_LABEL).get_attribute("class")
        AssertSearch.assert_value_in_data_type('is-checked', dark_mode_label_classes)

        # Click on the Font Size dropdown
        search_page.when_user_clicks_on_item(SearchPageLocators.FONT_SIZE_DROPDOWN)
        # Change to a random font size
        font_size_childs_options = browser.find_elements(*SearchPageLocators.FONT_SIZE_DROPDOWN_OPTIONS)
        rd_font_size_index = search_page.then_get_rnd_number(0, 4)
        font_size_childs_options[rd_font_size_index].click()

        # Click on the Font dropdown
        search_page.when_user_clicks_on_item(SearchPageLocators.FONT_FAMILY_DROPDOWN)
        # Change to a random Font
        font_family_childs_options = browser.find_elements(*SearchPageLocators.FONT_FAMILY_DROPDOWN_OPTIONS)
        rd_font_family_index = search_page.then_get_rnd_number(0, 13)
        font_family_childs_options[rd_font_family_index].click()

        # Click on the Display Language dropdown
        search_page.when_user_clicks_on_item(SearchPageLocators.LANGUAGE_DROPDOWN)
        # Change the value to "Hungarian"
        search_page.when_user_clicks_on_item(SearchPageLocators.LANGUAGE_HUNGARIAN)

        # Click again on the Settings:
        search_page.when_user_clicks_on_item(SearchPageLocators.SETTINGS_LINK)

        # Click on the Infinite Scroll flipper
        search_page.when_user_clicks_on_item(SearchPageLocators.INFINITY_SCROLL_TOGGLE)

        # Assert that the grandparent div of label[for="setting_kav"]
        # has the "is-checked" class
        inf_scroll_gparent_cls_list = search_page.then_get_attribute_for_item(
            SearchPageLocators.INFINITY_SCROLL_GPARENT_DIV, "class")

        AssertSearch.assert_value_in_data_type('is-checked', inf_scroll_gparent_cls_list)

        # Click on the Open Links in a New Tab flipper, it should be turned on
        search_page.when_user_clicks_on_item(SearchPageLocators.OPEN_LINKS_TOGGLE)
        open_new_gparent_cls_list = search_page.then_get_attribute_for_item(
            SearchPageLocators.OPEN_LINKS_GPARENT_DIV, "class")

        # Assert that  the div.frm__field (grandparent) of Open New has the
        # is-checked class
        AssertSearch.assert_value_in_data_type('is-checked', open_new_gparent_cls_list)

        # Click on the Reset buttons
        search_page.when_user_clicks_on_item(SearchPageLocators.APPEARANCE_RESET_LINK)
        search_page.when_user_clicks_on_item(SearchPageLocators.GENERAL_RESET_LINK)

        # Again click on the Settings
        search_page.when_user_clicks_on_item(SearchPageLocators.SETTINGS_LINK)

        # Assert that Light Mode Label has the "is-checked" class
        light_mode_label_cls_list = search_page.then_get_attribute_for_item(
            SearchPageLocators.LIGHT_MODE_LABEL, "class")
        AssertSearch.assert_value_in_data_type('is-checked', light_mode_label_cls_list)

        # Assert that the grandparent div of Infinity Scroll
        # does not have the "is-checked" class
        inf_scroll_gparent_cls_list = search_page.then_get_attribute_for_item(
            SearchPageLocators.INFINITY_SCROLL_GPARENT_DIV, "class")
        AssertSearch.assert_value_not_in_data_type('is-checked', inf_scroll_gparent_cls_list)

        # Assert that grandparent of Open New Tab
        # does not have the is-checked class
        open_new_gparent_cls_list = search_page.then_get_attribute_for_item(
            SearchPageLocators.OPEN_LINKS_GPARENT_DIV, "class")
        AssertSearch.assert_value_not_in_data_type('is-checked', open_new_gparent_cls_list)

    def test_random_article(self, browser):
        search_page = DuckDuckGoSearchPage(browser)
        result_page = DuckDuckGoSearchResult(browser)

        # WHEN the user searches for "phrase"
        search_page.when_user_searches(self.PHRASE)

        # AND: Click on search result
        search_page.when_user_clicks_on_rnd_search_result()

        # THEN assert search result contains 'Phrase' in title
        # assert self.PHRASE in result_page.then_get_title().lower()
        result_page_title = result_page.then_get_title().lower()
        AssertSearch.assert_value_in_data_type(self.PHRASE, result_page_title)

    def test_autocomplete_search(self, browser):
        # GIVEN the DuckDuckGo home page is displayed
        search_page = DuckDuckGoSearchPage(browser)

        # WHEN the user searches for "panda"
        autocomplete_result_list = search_page.when_user_enters_phrase_in_search_autocomplete(self.PHRASE)
        # THEN Assert if the autocomplete results contain the 'phrase'
        for auto_c_item in autocomplete_result_list:
            # assert self.PHRASE in auto_c_item.text
            AssertSearch.assert_value_in_data_type(self.PHRASE, auto_c_item.text)

        # AND Randomly click on one of the autocomplete suggestion results
        search_page.then_click_on_autocomplete_result(autocomplete_result_list)
