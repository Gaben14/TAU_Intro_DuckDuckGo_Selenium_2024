"""
This module contains DuckDuckGoImageSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.search import DuckDuckGoSearchPage


class DuckDuckGoImageSearch(DuckDuckGoSearchPage):
    pass

