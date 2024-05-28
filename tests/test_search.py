"""
These tests (test cases) cover DuckDuckGo searches.
"""
import pytest

from pages.result import DuckDuckGoSearchResult
from pages.search import DuckDuckGoSearchPage
from assertions.assert_search import AssertSearch

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
