from logs.logger import log_details

from selenium.webdriver.chrome.webdriver import WebDriver
from assertions.assert_search import AssertSearch

import datetime as dt

class DuckDuckGoSearchValidation:

    def __init__(self, browser: WebDriver):
        # assigning the browser fixture to self
        self.browser = browser

    # Used for the screenshots.
    TODAY = dt.datetime.today()
    """
    For screenshots, the first idea is to enable the save screenshots in every then_ method.
    Second idea would be to add it to the logs/logger.py file and import the WebDriver there
    """

    # Asserts
    def then_assert_variable_is_equal_to_variable(self, variable_1, variable_2):
        if variable_1 == "" or variable_1 is None:
            log_details().error(f"Variable can't be empty or NoneType!")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}"
                                         f"-{variable_1}.png")

        if variable_2 == "" or variable_2 is None:
            log_details().error(f"Variable can't be empty or NoneType!")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{variable_2}.png")

        AssertSearch.assert_variable_is_equal_to_variable(variable_1, variable_2)

    def then_assert_search_result_is_greater_as_0(self, search_result):
        if search_result == "" or search_result is None:
            log_details().error(f"Search_result can't be empty or NoneType!")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{search_result}.png")

        AssertSearch.assert_search_result_is_greater_as_0(search_result)

    def then_assert_value_in_data_type(self, value, data_type):
        if value == "" or value is None:
            log_details().error(f"Value can't be empty!")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{value}.png")

        if data_type == "" or data_type is None:
            log_details().error(f"Data_type can't be empty or NoneType!")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{data_type}.png")

        AssertSearch.assert_value_in_data_type(value, data_type)

    def then_assert_value_not_in_data_type(self, value, data_type):
        if value == "" or value is None:
            log_details().error(f"Value can't be empty!")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{value}.png")

        if data_type == "" or data_type is None:
            log_details().error(f"Data_type can't be empty or NoneType!")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{data_type}.png")

        AssertSearch.assert_value_not_in_data_type(value, data_type)

    # Asserts for an html element
    def then_assert_value_is_equal_to_html_element_attr(self, locator, attribute, value):
        # Method should take in the selector and just return the class_list
        html_element = self.browser.find_element(*locator)
        html_element_attr = html_element.get_attribute(attribute)

        if locator == "" or locator is None:
            log_details().error(f"Locator: {locator} is invalid")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{locator}.png")

        if attribute == "" or attribute is None:
            log_details().error(f"attribute: {attribute} is invalid")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{attribute}.png")

        if value == "" or value is None:
            log_details().error(f"value: {value} is invalid")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{value}.png")

        if html_element_attr is None:
            log_details().error(f"Invalid attribute!{locator[1]} "
                                     f"does not have the attribute: {attribute}")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{html_element_attr}.png")

        AssertSearch.assert_variable_is_equal_to_variable(
            value, html_element_attr)

    def then_assert_value_in_html_element(self, locator, attribute, value):
        # Method should take in the selector and just return the class_list
        html_element = self.browser.find_element(*locator)
        html_element_attr = html_element.get_attribute(attribute)

        if locator == "" or locator is None:
            log_details().error(f"Locator: {locator} is invalid")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{locator}.png")

        if attribute == "" or attribute is None:
            log_details().error(f"attribute: {attribute} is invalid")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{attribute}.png")

        if value == "" or value is None:
            log_details().error(f"value: {value} is invalid")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{value}.png")

        if html_element_attr is None:
            log_details().error(f"Invalid attribute!{locator[1]} "
                                     f"does not have the attribute: {attribute}")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{html_element_attr}.png")

        AssertSearch.assert_value_in_data_type(
            value, html_element_attr)

    def then_assert_value_not_in_html_element_attr(self, locator, attribute, value):
        html_element = self.browser.find_element(*locator)
        html_element_attr = html_element.get_attribute(attribute)

        if locator == "" or locator is None:
            log_details().error(f"Locator: {locator} is invalid")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{locator}.png")

        if attribute == "" or attribute is None:
            log_details().error(f"attribute: {attribute} is invalid")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{attribute}.png")

        if value == "" or value is None:
            log_details().error(f"value: {value} is invalid")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{value}.png")

        if html_element_attr is None:
            log_details().error(f"Invalid attribute!{locator[1]} "
                                     f"does not have the attribute: {attribute}")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{html_element_attr}.png")

        AssertSearch.assert_value_not_in_data_type(
            value, html_element_attr)

    def then_assert_html_element_has_is_checked_cls(self, locator):
        html_element = self.browser.find_element(*locator)
        html_element_cls = html_element.get_attribute('class')

        if html_element_cls is None:
            log_details().error(f"Invalid attribute!{locator[1]} "
                                     f"does not have the attribute: class")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{html_element_cls}.png")

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

        if html_element_cls is None:
            log_details().error(f"Invalid attribute!{locator[1]} "
                                     f"does not have the attribute: class")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{html_element_cls}.png")

        self.then_assert_value_in_data_type(
            'is-selected', html_element.get_attribute('class'))

    # Assert if a html element has no specific class in it:
    def then_assert_html_element_does_not_have_is_checked_cls(self, locator):
        html_element = self.browser.find_element(*locator)
        html_element_cls = html_element.get_attribute('class')

        if html_element_cls is None:
            log_details().error(f"Invalid attribute!{locator[1]} "
                                     f"does not have the attribute: class")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{html_element_cls}.png")

        self.then_assert_value_not_in_data_type(
            'is-checked', html_element_cls)

    def then_assert_html_element_does_not_have_is_active_cls(self, locator):
        html_element = self.browser.find_element(*locator)
        html_element_cls = html_element.get_attribute('class')

        if html_element_cls is None:
            log_details().error(f"Invalid attribute!{locator[1]} "
                                     f"does not have the attribute: class")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{html_element_cls}.png")

        self.then_assert_value_not_in_data_type(
            'is-active', html_element_cls)

    def then_assert_html_element_does_not_have_is_selected_cls(self, locator):
        html_element = self.browser.find_element(*locator)
        html_element_cls = html_element.get_attribute('class')

        if html_element_cls is None:
            log_details().error(f"Invalid attribute!{locator[1]} "
                                     f"does not have the attribute: class")
            self.browser.save_screenshot(f"logs/{self.TODAY.month:02d}-{self.TODAY.day:02d}-{self.TODAY.year}-"
                                         f"{html_element_cls}.png")

        self.then_assert_value_not_in_data_type(
            'is-selected', html_element_cls)
