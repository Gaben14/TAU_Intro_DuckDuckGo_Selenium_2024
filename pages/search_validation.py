from logs.log_configuration import log_details

from selenium.webdriver.chrome.webdriver import WebDriver
from assertions.assert_search import AssertSearch

class DuckDuckGoSearchValidation:

    def __init__(self, browser: WebDriver):
        # assigning the browser fixture to self
        self.browser = browser

    """
    For screenshots, the first idea is to enable the save screenshots in every then_ method.
    Second idea would be to add it to the logs/log_configuration.py file and import the WebDriver there
    """

    # Asserts
    def then_assert_variable_is_equal_to_variable(self, variable_1, variable_2):
        AssertSearch.assert_variable_is_equal_to_variable(variable_1, variable_2)

    def then_assert_search_result_is_greater_as_0(self, search_result):
        AssertSearch.assert_search_result_is_greater_as_0(search_result)

    def then_assert_value_in_data_type(self, value, data_type):
        AssertSearch.assert_value_in_data_type(value, data_type)

    def then_assert_value_not_in_data_type(self, value, data_type):
        AssertSearch.assert_value_not_in_data_type(value, data_type)

    # Asserts for an html element
    def then_assert_value_is_equal_to_html_element_attr(self, locator, attribute, value):
        # Method should take in the selector and just return the class_list
        html_element = self.browser.find_element(*locator)
        html_element_attr = html_element.get_attribute(attribute)

        AssertSearch.assert_variable_is_equal_to_variable(
            value, html_element_attr)

    def then_assert_value_in_html_element(self, locator, attribute, value):
        # Method should take in the selector and just return the class_list
        html_element = self.browser.find_element(*locator)
        html_element_attr = html_element.get_attribute(attribute)

        AssertSearch.assert_value_in_data_type(
            value, html_element_attr)

    def then_assert_value_not_in_html_element_attr(self, locator, attribute, value):
        html_element = self.browser.find_element(*locator)
        html_element_attr = html_element.get_attribute(attribute)

        AssertSearch.assert_value_not_in_data_type(
            value, html_element_attr)

    def then_assert_html_element_has_is_checked_cls(self, locator):
        html_element = self.browser.find_element(*locator)
        html_element_cls = html_element.get_attribute('class')

        self.then_assert_value_in_data_type(
            'is-checked', html_element_cls)

    def then_assert_html_element_has_is_active_cls(self, locator):
        html_element = self.browser.find_element(*locator)
        html_element_cls = html_element.get_attribute('class')

        if html_element_cls is None:
            log_details().error(f"Invalid attribute!{locator[1]} "
                                     f"does not have the attribute: class")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{html_element_cls}.png")

        self.then_assert_value_in_data_type(
            'is-active', html_element_cls)

    def then_assert_html_element_has_is_selected_cls(self, locator):
        html_element = self.browser.find_element(*locator)
        html_element_cls = html_element.get_attribute('class')

        self.then_assert_value_in_data_type(
            'is-selected', html_element_cls)

    # Assert if a html element has no specific class in it:
    def then_assert_html_element_does_not_have_is_checked_cls(self, locator):
        html_element = self.browser.find_element(*locator)
        html_element_cls = html_element.get_attribute('class')

        self.then_assert_value_not_in_data_type(
            'is-checked', html_element_cls)

    def then_assert_html_element_does_not_have_is_active_cls(self, locator):
        html_element = self.browser.find_element(*locator)
        html_element_cls = html_element.get_attribute('class')

        self.then_assert_value_not_in_data_type(
            'is-active', html_element_cls)

    def then_assert_html_element_does_not_have_is_selected_cls(self, locator):
        html_element = self.browser.find_element(*locator)
        html_element_cls = html_element.get_attribute('class')

        self.then_assert_value_not_in_data_type(
            'is-selected', html_element_cls)
