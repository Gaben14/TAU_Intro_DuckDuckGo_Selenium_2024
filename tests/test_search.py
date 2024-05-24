"""
These tests (test cases) cover DuckDuckGo searches.
"""
import pytest

from pages.result import DuckDuckGoSearchResult
from pages.search import DuckDuckGoSearchPage


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

        # GIVEN the DuckDuckGo home page is displayed

        # WHEN the user searches for "panda"
        search_page.search(self.PHRASE)

        # TODO: then_assert_something() or then_input_field_value_is(self.phrase)
        # TODO: move the asserts to different files and classes later
        # TODO: Google about moving the asserts to different classes and files.
        # THEN the search result query is "panda"
        assert self.PHRASE == result_page.search_input_value()

        # AND the search result links pertain (relates) to "panda"
        titles = result_page.result_link_titles()
        matches = [t for t in titles if self.PHRASE.lower() in t.lower()]
        assert len(matches) > 0

        # AND the search result title contains "panda"
        assert self.PHRASE in result_page.title().lower()

        # AND click on more results:
        result_page.click_on_more_results()

    def test_random_article(self, browser):
        search_page = DuckDuckGoSearchPage(browser)
        result_page = DuckDuckGoSearchResult(browser)

        # WHEN the user searches for "phrase"
        search_page.search(self.PHRASE)

        # AND: Click on search result
        search_page.click_on_rnd_search_result()

        # THEN assert search result contains 'Phrase' in title
        assert self.PHRASE in result_page.title().lower()

    def test_autocomplete_search(self, browser):
        # GIVEN the DuckDuckGo home page is displayed
        search_page = DuckDuckGoSearchPage(browser)

        # WHEN the user searches for "panda"
        autocomplete_result_list = search_page.search_autocomplete(self.PHRASE)
        # THEN Assert if the autocomplete results contain the 'phrase'
        for auto_c_item in autocomplete_result_list:
            assert self.PHRASE in auto_c_item.text

        # AND Randomly click on one of the autocomplete suggestion results
        search_page.click_on_autocomplete_result(autocomplete_result_list)
