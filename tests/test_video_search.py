"""
These tests (test cases) cover DuckDuckGo video searches.
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from assertions.assert_search import AssertSearch
from pages.video_search import DuckDuckGoVideoSearch
from pages.search_validation import DuckDuckGoSearchValidation
from utils.locators_video import VideoPageLocators


class TestVideoSearch:
    """
    Test Case:

    1. Open the browser and the https://duckduckgo.com page - Assert if the page has been opened successfully -
    HTTP 200
    2. Find the search-bar. Enter the phrase.
    3. Click on the 'Videos' tab - Assert if Videos tab is active
    4. Change the value inside "Any times" to "Past Week"
        - Assert if value has been changed to "Past Week"
    5. Change the value inside "Any resolution" to "Standard definition"
        - Assert if "Standard definition" has the class "is-selected"
    6. Create a list which contains all the options from the "Any Duration" dropdown
        - Randomly change the value of the dropdown.
        - Assert if the value has changed.
    7. Change the license under the "Any License" dropdown to "YouTube standard"
        - Assert if the change has been successful
    8. Check if there is any search results after the change.
    9. Open one of the Results (random?) in a new tab, change to that tab.
        - Assert the title of the new tab contains the Phrase
        - Close the tab and navigate back to Video Page.
    """
    PHRASE = "panda"

    def test_video_tab(self, browser):
        video_search_page = DuckDuckGoVideoSearch(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        # Find the search-bar. Enter the phrase
        video_search_page.when_user_searches(self.PHRASE)

        # Click on the Videos tab
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_TAB)

        # Get class list after click
        search_page_validation.then_assert_html_element_has_is_active_cls(
            VideoPageLocators.VIDEO_TAB)


    def test_change_video_post_date(self, browser):
        video_search_page = DuckDuckGoVideoSearch(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        # Find the search-bar. Enter the phrase
        video_search_page.when_user_searches(self.PHRASE)

        # Click on the Videos tab
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_TAB)

        # Click on the "Any Date" dropdown
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_UPLOAD_DATE_DROPDOWN)

        # Click on the "Past week" value
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_PAST_WEEK)

        # Assert if the first (<a>) child of the VIDEO_UPLOAD_DATE_DROPDOWN has the text "Past Week"
        search_page_validation.then_assert_value_in_html_element(
            VideoPageLocators.VIDEO_UPLOAD_DATE_DROPDOWN_CHILD_LINK, 'innerHTML', 'Past week')

    def test_change_video_resolution(self, browser):
        video_search_page = DuckDuckGoVideoSearch(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        # Find the search-bar. Enter the phrase
        video_search_page.when_user_searches(self.PHRASE)

        # Click on the Videos tab
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_TAB)

        # Click on the "Any resolution" dropdown
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_RESOLUTION_DROPDOWN)

        # Click on the "Standard Definition"
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_STAND_DEF)

        # Assert if "Standard definition" has the class is-selected
        search_page_validation.then_assert_html_element_has_is_selected_cls(
            VideoPageLocators.VIDEO_STAND_DEF)

    def test_change_video_duration(self, browser):
        video_search_page = DuckDuckGoVideoSearch(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        # Find the search-bar. Enter the phrase
        video_search_page.when_user_searches(self.PHRASE)

        # Click on the Videos tab
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_TAB)

        # Click on the "Any Duration" dropdown
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_DURATION_DROPDOWN)

        # Get all the child items of "Any duration"
        video_duration_childs = video_search_page.then_get_all_child_items(
            VideoPageLocators.VIDEO_DURATION_DROPDOWN_OPTIONS)

        # Randomly select one of the items, random should be between 1-3
        # because 0 index of the dropdown is "Any duration"
        rand_int = video_search_page.then_get_rnd_number(1, len(video_duration_childs))
        # Get the innerHTML or text value of the random child
        rand_child_innerHTML = video_duration_childs[rand_int].get_attribute("text")
        video_duration_childs[rand_int].click()

        # Assert that the child <a> item's text of "Any duration" dropdown is
        # the same as for the random item, we check if the value has actually changed.
        search_page_validation.then_assert_value_is_equal_to_html_element(
            VideoPageLocators.VIDEO_DURATION_DROPDOWN_CHILD_LINK, 'text', rand_child_innerHTML)

    def test_change_video_license(self, browser):
        video_search_page = DuckDuckGoVideoSearch(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        # Find the search-bar. Enter the phrase
        video_search_page.when_user_searches(self.PHRASE)

        # Click on the Videos tab
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_TAB)

        # Click on the "Any license" dropdown:
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_LICENSE_DROPDOWN)

        # After that click on the "YouTube Standard":
        video_search_page.when_user_clicks_on_item(VideoPageLocators.YOUTUBE_STANDARD_LINK)

        # Assert that value has changed to "YouTube Standard":
        search_page_validation.then_assert_value_is_equal_to_html_element(
            VideoPageLocators.VIDEO_LICENSE_DROPDOWN_CHILD_LINK, 'innerHTML', 'YouTube Standard')

    def test_search_results_after_filtering(self, browser):
        video_search_page = DuckDuckGoVideoSearch(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        # Find the search-bar. Enter the phrase
        video_search_page.when_user_searches(self.PHRASE)

        # Click on the Videos tab
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_TAB)

        # Click on the "Any time" dropdown, select one value randomly
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_UPLOAD_DATE_DROPDOWN)
        video_date_dd_options = video_search_page.then_get_all_child_items(
            VideoPageLocators.VIDEO_UPLOAD_DATE_DROPDOWN_OPTIONS)
        rd_date_index = video_search_page.then_get_rnd_number(1, len(video_date_dd_options))
        video_date_dd_options[rd_date_index].click()

        # Click on the "Any resolution" dropdown, select one value randomly
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_RESOLUTION_DROPDOWN)
        video_res_dd_options = video_search_page.then_get_all_child_items(
            VideoPageLocators.VIDEO_RESOLUTION_DROPDOWN_OPTIONS)
        rd_res_index = video_search_page.then_get_rnd_number(1, len(video_res_dd_options))
        video_res_dd_options[rd_res_index].click()

        # Click on the "Any duration" dropdown, select one value randomly
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_DURATION_DROPDOWN)
        video_dur_dd_options = video_search_page.then_get_all_child_items(
            VideoPageLocators.VIDEO_DURATION_DROPDOWN_OPTIONS)
        rd_dur_index = video_search_page.then_get_rnd_number(1, len(video_dur_dd_options))
        video_dur_dd_options[rd_dur_index].click()

        # Click on the "Any license" dropdown, select one value randomly
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_LICENSE_DROPDOWN)
        video_lic_dd_options = video_search_page.then_get_all_child_items(
            VideoPageLocators.VIDEO_LICENSE_DROPDOWN_OPTIONS)
        rd_lic_index = video_search_page.then_get_rnd_number(1, len(video_lic_dd_options))
        video_lic_dd_options[rd_lic_index].click()

        # Assert if there are any results after these changes
        video_results = video_search_page.then_get_all_child_items(
            VideoPageLocators.VIDEO_SEARCH_RESULTS)

        # AssertSearch.assert_search_result_is_greater_as_0(len(video_results))
        search_page_validation.then_assert_search_result_is_greater_as_0(len(video_results))

    def test_open_result_in_new_tab(self, browser):
        video_search_page = DuckDuckGoVideoSearch(browser)
        search_page_validation = DuckDuckGoSearchValidation(browser)

        # Find the search-bar. Enter the phrase
        video_search_page.when_user_searches(self.PHRASE)

        # Click on the Videos tab
        video_search_page.when_user_clicks_on_item(VideoPageLocators.VIDEO_TAB)

        # Get All Results and open it in a new browser tab:
        video_link_results = video_search_page.then_get_all_child_items(
            VideoPageLocators.VIDEO_SEARCH_RESULTS_LINK)

        video_rnd_index = video_search_page.then_get_rnd_number(0, len(video_link_results))
        # Inside the Video Result, get the attribute for the href,
        # use that href value to open a new browser tab
        video_result_href = video_link_results[video_rnd_index].get_attribute("href")

        browser.execute_script("window.open('about:blank','secondtab');")
        browser.switch_to.window("secondtab")
        browser.get(video_result_href)

        # Wait for the "Accept All" button to become visible
        accept_all = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located(VideoPageLocators.YOUTUBE_ACCEPT_ALL_BTN)
        )
        accept_all.click()

        # Assert in the new tab that title contains the PHRASE
        phrase_in_second_tab_title = WebDriverWait(browser, 15).until(
            lambda title_check: self.PHRASE in browser.title.lower()
        )

        search_page_validation.then_assert_variable_is_equal_to_variable(True, phrase_in_second_tab_title)
