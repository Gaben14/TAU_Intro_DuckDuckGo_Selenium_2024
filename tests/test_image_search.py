"""
These tests (test cases) cover DuckDuckGo image searches.
"""
import requests
from selenium.webdriver.common.by import By

from pages.result import DuckDuckGoSearchResult
from pages.image_search import DuckDuckGoImageSearch
from pages.search import DuckDuckGoSearchPage

class TestImageSearch:
    """
    Test Case:

    1. Open the browser and the https://duckduckgo.com page - Assert if the page has been opened successfully - HTTP 200
    2. Find the search-bar. Enter the phrase.
    3. Click on the 'Images' tab - Assert if Images tab is active
    4. Change the value inside "All sizes" to "Medium" - Assert if value has been changed to Medium
    5. Create a list which contains all the color options from the "All colors" dropdown
        5.1 Change the value inside "All Colors" to a random value from the previously created list
        5.2 Assert if the color has been changed.
    6. Change the type under the "All types" dropdown to "Animated GIF"
        6.1 Assert if the change has been successful
    7. Change the "All Licenses" to "Free to Share and Use" - Assert if there are any images after this change.
    """

    # Class Variable
    PHRASE = "panda"

    def test_images_tab(self, browser, get_url):
        image_search_page = DuckDuckGoImageSearch(browser, get_url)
        result_page = DuckDuckGoSearchResult(browser)

        # Temporarly moving the locators here
        IMAGES_TAB = (By.CSS_SELECTOR, '[data-testid="tab-label-images"]')
        IMAGE_SIZE_DROPDOWN = (By.CLASS_NAME, 'dropdown--size')
        IMAGE_SIZE_MEDIUM = (By.CSS_SELECTOR, 'a[data-value="Medium"]')

        response = requests.get(get_url)
        # Assert if the page can be pinged successfully - HTTP 200
        # TODO: If the status code is not 200, the test should not open the browser!
        assert response.status_code == 200

        # If the home page can be pinged, open the browser.
        image_search_page.load()

        # Find the search-bar. Enter the phrase.
        image_search_page.search(self.PHRASE)

        # Click on the images tab.
        image_search_page.click_on_images_tab()

        # Assert that the images tab has been selected. - check if the <a> tag has the is-active class
        assert 'is-active' in image_search_page.html_css_class_list(IMAGES_TAB)

        # Change the Image Size
        image_search_page.change_image_size()

        # Assert that the 'is-selected' class can be found on the Image Size Medium Button
        assert 'is-selected' in image_search_page.html_css_class_list(IMAGE_SIZE_MEDIUM)
