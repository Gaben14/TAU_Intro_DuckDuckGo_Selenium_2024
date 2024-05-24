"""
These tests (test cases) cover DuckDuckGo image searches.
"""
import requests

from pages.image_search import DuckDuckGoImageSearch
from utils import locators_image


class TestImageSearch:
    """
    Test Case:

    1. Open the browser and the https://duckduckgo.com page - Assert if the page has been opened successfully - HTTP 200
    2. Find the search-bar. Enter the phrase.
    3. Click on the 'Images' tab - Assert if Images tab is active
    4. Change the value inside "All sizes" to "Medium" - Assert if value has been changed to Medium
    5. Create a list which contains all the color options from the "All colors" dropdown
        5.1 Assert if the color has been changed.
    6. Change the type under the "All types" dropdown to "Animated GIF"
        6.1 Assert if the change has been successful
    7. Change the "All Licenses" to "Free to Share and Use"
        7.1 - Assert if "Free to Share and Use" is now selected
        7.2 - Assert if there are any images / results after this change.
    """

    # Class Variables
    PHRASE = "panda"

    def test_images_tab(self, browser):
        """
        response = requests.get()
        # Assert if the page can be pinged successfully - HTTP 200
        # TODO: If the status code is not 200, the test should not open the browser!
        assert response.status_code == 200
        # TODO: After the response code, wait until an item on the page has loaded
        """
        image_search_page = DuckDuckGoImageSearch(browser)
        # Find the search-bar. Enter the phrase.
        image_search_page.search(self.PHRASE)
        # Click on the images tab.
        image_search_page.click_on_item(locators_image.IMAGES_TAB)

        # Assert that the images tab has been selected. - check if the <a> tag has the is-active class
        assert 'is-active' in image_search_page.get_html_css_class_list(locators_image.IMAGES_TAB)

    def test_change_image_size(self, browser):
        # Change the Image Size

        image_search_page = DuckDuckGoImageSearch(browser)

        # Search for phrase
        image_search_page.search(self.PHRASE)
        # Click on the images tab.
        image_search_page.click_on_item(locators_image.IMAGES_TAB)

        image_search_page.change_image_size()
        image_size_medium_cls_list = image_search_page.get_html_css_class_list(locators_image.IMAGE_SIZE_MEDIUM)

        # Assert that the 'is-selected' class can be found on the Image Size Medium Button
        assert 'is-selected' in image_size_medium_cls_list

    def test_change_color(self, browser):
        # TEST: Change from "All Colors" to "Black and white" and validate if color has changed

        image_search_page = DuckDuckGoImageSearch(browser)

        # Search for phrase
        image_search_page.search(self.PHRASE)
        # Click on the images tab.
        image_search_page.click_on_item(locators_image.IMAGES_TAB)

        # Click on the 'All Colors' dropdown.
        image_search_page.click_on_item(locators_image.ALL_COLORS_DROPDOWN)

        image_search_page.click_on_item(locators_image.BLACK_AND_WHITE)
        black_and_white_cls_list = image_search_page.get_html_css_class_list(locators_image.BLACK_AND_WHITE)
        assert 'is-selected' in black_and_white_cls_list

    def test_change_type(self, browser):
        # TEST: Change from "All Types" to "Animated GIF" and validate if All Types has changed
        image_search_page = DuckDuckGoImageSearch(browser)

        # Search for phrase
        image_search_page.search(self.PHRASE)
        # Click on the images tab.
        image_search_page.click_on_item(locators_image.IMAGES_TAB)

        image_search_page.click_on_item(locators_image.ALL_TYPES)

        image_search_page.click_on_item(locators_image.ANIMATED_GIF)
        animated_gif_cls_list = image_search_page.get_html_css_class_list(locators_image.ANIMATED_GIF)
        assert 'is-selected' in animated_gif_cls_list

    def test_change_license(self, browser):
        """
        7. Change the "All Licenses" to "Free to Share and Use"
            7.1 - Assert if "Free to Share and Use" is now selected
            7.2 - Assert if there are any images / results after this change.
        """
        image_search_page = DuckDuckGoImageSearch(browser)

        # Search for phrase
        image_search_page.search(self.PHRASE)

        image_search_page.click_on_item(locators_image.IMAGES_TAB)

        image_search_page.click_on_item(locators_image.ALL_LICENSES_DROPDOWN)

        image_search_page.click_on_item(locators_image.FREE_TO_SHARE_AND_USE_LINK)

        # 7.1 - Assert if "Free to Share and Use" is now selected
        link_in_dropdown = image_search_page.get_child_link_of_dropdown_menu('license')
        assert link_in_dropdown.get_attribute("innerHTML") == "Free to Share and Use"

        # 7.2 - Assert if there are any images / results after this change.
        image_results = image_search_page.get_img_results()
        assert image_results > 0
