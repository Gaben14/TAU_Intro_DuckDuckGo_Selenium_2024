from logs.logger import log_details

class AssertSearch:
    @staticmethod
    def assert_value_not_in_data_type(value, data_type):
        try:
            assert value not in data_type
        except AssertionError:
            log_details().critical(f"Assertion Error! "
                                   f"Value {value} can be found in {data_type} "
                                   f"by default {value} should not be {data_type}!")
    @staticmethod
    def assert_value_in_data_type(value, data_type):
        try:
            assert value in data_type
        except AssertionError:
            log_details().critical(f"Assertion Error! "
                                   f"Value {value} can't be found in {data_type} "
                                   f"by default {value} should be {data_type}!")

    @staticmethod
    def assert_search_result_is_greater_as_0(search_results):
        try:
            assert search_results > 0
        except AssertionError:
            log_details().critical(f"Assertion Error! "
                                   f"Search results {search_results} has no values!"
                                   f"{search_results} should be > 0")

    @staticmethod
    def assert_variable_is_equal_to_variable(value_1, value_2):
        try:
            assert value_1 == value_2
        except AssertionError:
            log_details().critical(f"Assertion Error! "
                                   f"Value_1: {value_1} is not equal to Value_2: {value_2}")
