"""
These tests (test cases) cover DuckDuckGo searches.
"""
import pytest

from pages.result import DuckDuckGoSearchResult
from pages.search import DuckDuckGoSearchPage


class TestSearch:
    # Class Variable
    PHRASE = "panda"

    # @pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
    def test_basic_duckduckgo_search(self, browser):  # phrase
        search_page = DuckDuckGoSearchPage(browser)
        result_page = DuckDuckGoSearchResult(browser)

        # GIVEN the DuckDuckGo home page is displayed
        search_page.load()

        # WHEN the user searches for "panda"
        search_page.search(self.PHRASE)

        # THEN the search result query is "panda"
        assert self.PHRASE == result_page.search_input_value()

        # AND the search result links pertain (relates) to "panda"
        titles = result_page.result_link_titles()
        matches = [t for t in titles if self.PHRASE.lower() in t.lower()]
        assert len(matches) > 0

        # AND the search result title contains "panda"
        assert self.PHRASE in result_page.title()

        # AND click on more results:
        result_page.click_on_more_results()

    def test_random_article(self, browser):
        search_page = DuckDuckGoSearchPage(browser)

        # GIVEN the DuckDuckGo home page is displayed
        search_page.load()

        # WHEN the user searches for "panda"
        search_page.search(self.PHRASE)

        # AND: Click on search result
        search_page.click_on_search_result()

        # TODO: THEN assert search result contains 'Phrase' in title

    def test_autocomplete_search(self, browser):
        # GIVEN the DuckDuckGo home page is displayed
        search_page = DuckDuckGoSearchPage(browser)

        search_page.load()
        # WHEN the user searches for "panda"
        autocomplete_result_list = search_page.search_autocomplete(self.PHRASE)
        # THEN Assert if the autocomplete results contain the 'phrase'
        for auto_c_item in autocomplete_result_list:
            assert self.PHRASE in auto_c_item.text

        # AND Randomly click on one of the autocomplete suggestion results
        search_page.click_on_autocomplete_result(autocomplete_result_list)
