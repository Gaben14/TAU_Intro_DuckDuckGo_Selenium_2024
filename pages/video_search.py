"""
This module contains DuckDuckGoVideoSearchPage,
the page object for the DuckDuckGo Video search page.
"""

# imports:
from utils.locators_video import VideoPageLocators
from pages.search import DuckDuckGoSearchPage


class DuckDuckGoVideoSearch(DuckDuckGoSearchPage):

    # Constructor:
    def __init__(self, browser):
        # Call the __init__ of parent:
        super().__init__(browser)

    def then_get_all_child_items(self, child_locator):
        child_html_elements = self.browser.find_elements(*child_locator)
        return child_html_elements
