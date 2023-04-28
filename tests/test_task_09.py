import unittest
from task_09 import connect_dicts


class TestConnectDicts(unittest.TestCase):

    def test_connect_dicts_common_keys(self):
        first_dict = {'a': 13, 'b': 12, 'c': 5}
        second_dict = {'b': 11, 'd': 9, 'e': 18}

        expected_result = {'b': 11, 'a': 13, 'e': 18}
        self.assertEqual(connect_dicts(first_dict, second_dict), expected_result)

    def test_connect_dicts_the_same_keys_the_firs_dict_values_greater(self):
        first_dict = {'a': 3, 'b': 14, 'c': 5}
        second_dict = {'b': 17, 'd': 1, 'e': 2}

        expected_result = {'b': 14}
        self.assertEqual(connect_dicts(first_dict, second_dict), expected_result)

    def test_connect_dicts_the_same_keys_the_second_dict_values_greater(self):
        first_dict = {'a': 3, 'b': 17, 'c': 5}
        second_dict = {'b': 12, 'd': 10, 'e': 7}

        expected_result = {'d': 10, 'b': 12}
        self.assertEqual(connect_dicts(first_dict, second_dict), expected_result)

    def test_connect_dicts_no_common_keys(self):
        first_dict = {'a': 3, 'b': 4, 'c': 5}
        second_dict = {'b': 7, 'd': 1, 'e': 8}

        expected_result = {}
        self.assertEqual(connect_dicts(first_dict, second_dict), expected_result)

    def test_connect_dicts_second_dict_empty(self):
        first_dict = {'a': 5, 'b': 2, 'c': 15}
        second_dict = {}

        expected_result = {'c': 15}
        self.assertEqual(connect_dicts(first_dict, second_dict), expected_result)

    def test_connect_dicts_first_dict_empty(self):
        first_dict = {}
        second_dict = {'d': 1, 'e': 14}

        expected_result = {'e': 14}
        self.assertEqual(connect_dicts(first_dict, second_dict), expected_result)

    def test_connect_dicts_both_dicts_empty(self):
        first_dict = {}
        second_dict = {}

        expected_result = {}
        self.assertEqual(connect_dicts(first_dict, second_dict), expected_result)
