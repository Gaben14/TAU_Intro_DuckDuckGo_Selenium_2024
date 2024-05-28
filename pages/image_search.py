"""
This module contains DuckDuckGoImageSearchPage,
the page object for the DuckDuckGo Image search page.
"""

from utils.locators_image import ImagePageLocators
from pages.search import DuckDuckGoSearchPage


class DuckDuckGoImageSearch(DuckDuckGoSearchPage):

    # Constructor:
    def __init__(self, browser):
        # Call the __init__ of parent:
        super().__init__(browser)

    # Methods, use BDD words before the method names:
    # Example: when_change_image_size
    def when_user_changes_image_size(self):
        # Change the value inside "All sizes" to "Medium"
        image_size_dropdown = self.browser.find_element(*ImagePageLocators.IMAGE_SIZE_DROPDOWN)
        image_size_dropdown.click()
        image_size_medium = self.browser.find_element(*ImagePageLocators.IMAGE_SIZE_MEDIUM)
        image_size_medium.click()

    # Get all image results:
    def then_get_img_results(self):
        img_results = self.browser.find_elements(*ImagePageLocators.IMG_RESULTS)
        return len(img_results)

