import logging
import datetime as dt

from selenium.webdriver.chrome.webdriver import WebDriver
from assertions.assert_search import AssertSearch

class DuckDuckGoSearchValidation:

    def __init__(self, browser: WebDriver):
        # assigning the browser fixture to self
        self.browser = browser

    def log_details(self):
        # Logging
        # Get the logger and set its level
        today = dt.datetime.today()
        log_filename = f"{today.month:02d}-{today.day:02d}-{today.year}.log"

        logger = logging.getLogger("searchLog")
        logger.setLevel(logging.ERROR)

        # Create handlers
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(f"logs/{log_filename}")

        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s"
        )

        # Add the formatter to the handlers:
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger

    # Asserts
    def then_assert_variable_is_equal_to_variable(self, variable_1, variable_2):
        AssertSearch.assert_variable_is_equal_to_variable(variable_1, variable_2)

    def then_assert_search_result_is_greater_as_0(self, search_result):
        AssertSearch.assert_search_result_is_greater_as_0(search_result)
        self.log_details().debug("This message is a Debug message")

    def then_assert_value_in_data_type(self, value, data_type):
        AssertSearch.assert_value_in_data_type(value, data_type)

    def then_assert_value_not_in_data_type(self, value, data_type):
        AssertSearch.assert_value_not_in_data_type(value, data_type)

    # Asserts for an html element
    def then_assert_value_is_equal_to_html_element(self, locator, attribute, value):
        # Method should take in the selector and just return the class_list
        html_element = self.browser.find_element(*locator)
        AssertSearch.assert_variable_is_equal_to_variable(value, html_element.get_attribute(attribute))

    def then_assert_value_in_html_element(self, locator, attribute, value):
        # Method should take in the selector and just return the class_list
        html_element = self.browser.find_element(*locator)
        AssertSearch.assert_value_in_data_type(value, html_element.get_attribute(attribute))

    def then_assert_value_not_in_html_element(self, locator, attribute, value):
        html_element = self.browser.find_element(*locator)
        AssertSearch.assert_value_not_in_data_type(value, html_element.get_attribute(attribute))

    def then_assert_html_element_has_is_checked_cls(self, locator):
        html_element = self.browser.find_element(*locator)

        self.then_assert_value_in_data_type('is-checked', html_element.get_attribute('class'))

    def then_assert_html_element_has_is_active_cls(self, locator):
        html_element = self.browser.find_element(*locator)

        self.then_assert_value_in_data_type('is-active', html_element.get_attribute('class'))

    def then_assert_html_element_has_is_selected_cls(self, locator):
        html_element = self.browser.find_element(*locator)

        self.then_assert_value_in_data_type('is-selected', html_element.get_attribute('class'))

    # Assert if a html element has no specific class in it:
    def then_assert_data_type_does_not_have_is_checked(self, locator):
        html_element = self.browser.find_element(*locator)

        self.then_assert_value_not_in_data_type('is-checked', html_element.get_attribute('class'))

    def then_assert_data_type_does_not_have_is_active(self, locator):
        html_element = self.browser.find_element(*locator)

        self.then_assert_value_not_in_data_type('is-active', html_element.get_attribute('class'))

    def then_assert_data_type_does_not_have_is_selected(self, locator):
        html_element = self.browser.find_element(*locator)

        self.then_assert_value_not_in_data_type('is-selected', html_element.get_attribute('class'))
