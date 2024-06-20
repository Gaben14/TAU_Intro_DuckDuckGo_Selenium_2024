"""
These tests (test cases) cover DuckDuckGo image searches.
"""

from pages.image_search import DuckDuckGoImageSearch
from utils.locators_image import ImagePageLocators
from pages.search_validation import DuckDuckGoSearchValidation


class TestImageSearch:
    """
    Test Case:

    1. Open the browser and the https://duckduckgo.com page - Assert if the page has been opened successfully - HTTP 200
    2. Find the search-bar. Enter the phrase.
    3. Click on the 'Images' tab - Assert if Images tab is active
    4. Change the value inside "All sizes" to "Medium"
        - Assert if value has been changed to Medium
    5. Create a list which contains all the color options from the "All colors" dropdown
        - Assert if the color has been changed.
    6. Change the type under the "All types" dropdown to "Animated GIF"
        - Assert if the change has been successful
    7. Change the "All Licenses" to "Free to Share and Use"
        - Assert if "Free to Share and Use" is now selected
        - Assert if there are any images / results after this change.
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
        search_page_validation = DuckDuckGoSearchValidation(browser)
        # Find the search-bar. Enter the phrase.
        image_search_page.when_user_searches(self.PHRASE)
        # Click on the images tab.
        image_search_page.when_user_clicks_on_item(ImagePageLocators.IMAGES_TAB)

        # Assert that Images Tab now has the 'is-active' class
        search_page_validation.then_assert_html_element_has_is_active_cls(
            ImagePageLocators.IMAGES_TAB)

    def test_change_image_size(self, browser):
        # Change the Image Size
        image_search_page = DuckDuckGoImageSearch(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        # Search for phrase
        image_search_page.when_user_searches(self.PHRASE)
        # Click on the images tab.
        image_search_page.when_user_clicks_on_item(ImagePageLocators.IMAGES_TAB)

        # Change Image Size
        image_search_page.when_user_changes_image_size()

        # Assert that the 'is-selected' class can be found on the Image Size Medium Button
        search_page_validation.then_assert_html_element_has_is_selected_cls(
            ImagePageLocators.IMAGE_SIZE_MEDIUM)

    def test_change_color(self, browser):
        # TEST: Change from "All Colors" to "Black and white" and validate if color has changed
        image_search_page = DuckDuckGoImageSearch(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        # Search for phrase
        image_search_page.when_user_searches(self.PHRASE)

        # Click on the images tab.
        image_search_page.when_user_clicks_on_item(ImagePageLocators.IMAGES_TAB)

        # Click on the 'All Colors' dropdown.
        image_search_page.when_user_clicks_on_item(ImagePageLocators.ALL_COLORS_DROPDOWN)

        image_search_page.when_user_clicks_on_item(ImagePageLocators.BLACK_AND_WHITE)

        search_page_validation.then_assert_html_element_has_is_selected_cls(
            ImagePageLocators.BLACK_AND_WHITE)

    def test_change_type(self, browser):
        # Change from "All Types" to "Animated GIF" and validate if all Types has changed
        image_search_page = DuckDuckGoImageSearch(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        # Search for phrase
        image_search_page.when_user_searches(self.PHRASE)
        # Click on the images tab.
        image_search_page.when_user_clicks_on_item(ImagePageLocators.IMAGES_TAB)

        image_search_page.when_user_clicks_on_item(ImagePageLocators.ALL_TYPES)

        image_search_page.when_user_clicks_on_item(ImagePageLocators.ANIMATED_GIF)

        # assert 'is-selected' in ANIMATED_GIF
        search_page_validation.then_assert_html_element_has_is_selected_cls(
            ImagePageLocators.ANIMATED_GIF)

    def test_change_license(self, browser):
        image_search_page = DuckDuckGoImageSearch(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        # Search for phrase
        image_search_page.when_user_searches(self.PHRASE)

        image_search_page.when_user_clicks_on_item(ImagePageLocators.IMAGES_TAB)

        image_search_page.when_user_clicks_on_item(ImagePageLocators.ALL_LICENSES_DROPDOWN)

        image_search_page.when_user_clicks_on_item(ImagePageLocators.FREE_TO_SHARE_AND_USE_LINK)

        # Assert if "Free to Share and Use" is now selected
        search_page_validation.then_assert_value_is_equal_to_html_element_attr(
            ImagePageLocators.FREE_TO_SHARE_AND_USE_LINK, 'innerHTML', 'Free to Share and Use')

        # Assert if there are any images / results after this change.
        image_results = image_search_page.then_get_img_results()

        # AssertSearch.assert_search_result_is_greater_as_0(image_results)
        search_page_validation.then_assert_search_result_is_greater_as_0(image_results)
