class AssertSearch:
    # TODO: Review if the then_assert should be used instead of assert in method names?
    @staticmethod
    def assert_value_not_in_data_type(value, data_type):
        assert value not in data_type
    @staticmethod
    def assert_value_in_data_type(value, data_type):
        assert value in data_type

    @staticmethod
    def assert_search_result_is_greater_as_0(search_results):
        assert search_results > 0

    @staticmethod
    def assert_variable_is_equal_to_variable(value_1, value_2):
        assert value_1 == value_2
