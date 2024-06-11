from selenium.webdriver.chrome.webdriver import WebDriver

from assertions.assert_search import AssertSearch


class DuckDuckGoSearchValidation:

    def __init__(self, browser: WebDriver):
        # assigning the browser fixture to self
        self.browser = browser
    # Asserts
    def then_assert_value_in_data_type(self, value, data_type):
        AssertSearch.assert_value_in_data_type(value, data_type)

    def then_assert_value_not_in_data_type(self, value, data_type):
        AssertSearch.assert_value_not_in_data_type(value, data_type)

    def then_assert_value_in_html_element(self, locator, attribute, value):
        # Method should take in the selector and just return the class_list
        html_element = self.browser.find_element(*locator)
        AssertSearch.assert_value_in_data_type(value, html_element.get_attribute(attribute))

    def then_assert_value_not_in_html_element(self, locator, attribute, value):
        html_element = self.browser.find_element(*locator)
        AssertSearch.assert_value_not_in_data_type(value, html_element.get_attribute(attribute))

    def then_assert_variable_is_equal_to_variable(self, variable_1, variable_2):
        AssertSearch.assert_variable_is_equal_to_variable(variable_1, variable_2)

    def then_assert_search_result_is_greater_as_0(self, search_result):
        AssertSearch.assert_search_result_is_greater_as_0(search_result)

    # Asserts if a html element has a specific class in it
    def then_assert_html_element_has_is_checked(self, locator):
        self.then_assert_value_in_html_element(locator, 'class', 'is-checked')

    def then_assert_html_element_has_is_active(self, locator):
        self.then_assert_value_in_html_element(locator, "class", "is-active")

    def then_assert_html_element_has_is_selected(self, locator):
        self.then_assert_value_in_html_element(locator, "class", "is-selected")

    # Assert if a html element has no specific class in it:
    def then_assert_html_element_has_no_is_checked(self, locator):
        self.then_assert_value_not_in_html_element(locator, "class", "is-checked")

    def then_assert_html_element_has_no_is_active(self, locator):
        self.then_assert_value_not_in_html_element(locator, "class", "is-active")

    def then_assert_html_element_has_no_is_selected(self, locator):
        self.then_assert_value_not_in_html_element(locator, "class", "is-selected")

    # TODO: Create seperate methods for the 'is-active' and 'is-selected' asserts
    # Example: then_item_is_active, then_item_is_selected
    # After that only these small methods should be called inside the test_ files.
    # Breakdown the logic into smaller methods / functions as possible --> They should be simple as possible
