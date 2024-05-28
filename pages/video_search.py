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

