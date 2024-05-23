"""
This module contains DuckDuckGoImageSearchPage,
the page object for the DuckDuckGo search page.
"""

from utils import locators_image
from pages.search import DuckDuckGoSearchPage


class DuckDuckGoImageSearch(DuckDuckGoSearchPage):

    # Constructor:
    def __init__(self, browser, get_url):
        # Call the __init__ of parent:
        super().__init__(browser, get_url)

    # Methods:
    # TODO: use BDD words before the method names:
    # TODO: when_change_image_size
    def change_image_size(self):
        # Change the value inside "All sizes" to "Medium"
        image_size_dropdown = self.browser.find_element(*locators_image.IMAGE_SIZE_DROPDOWN)
        image_size_dropdown.click()
        image_size_medium = self.browser.find_element(*locators_image.IMAGE_SIZE_MEDIUM)
        image_size_medium.click()

    # Get all child items under a dropdown:
    """
    def get_all_child_items_in_dropdown(self):
        # div.modal--dropdown--color a.modal__list__link
        dropdown_list = self.browser.find_elements(*locators_image.DROPDOWN_LIST)
        for item in dropdown_list:
            print(item)
    """
