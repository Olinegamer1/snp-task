import unittest
from tasks.task_04 import sort_list


class TestSortList(unittest.TestCase):

    def test_sort_list_regular_input(self):
        arr = [3, 1, 4, 2]
        expected_result = [3, 4, 1, 2, 1]
        result = sort_list(arr)
        self.assertEqual(result, expected_result)

    def test_sort_list_empty_input(self):
        arr = []
        expected_result = []
        result = sort_list(arr)
        self.assertEqual(result, expected_result)

    def test_sort_list_identical_elements(self):
        arr = [3, 3, 3, 3]
        expected_result = [3, 3, 3, 3, 3]
        result = sort_list(arr)
        self.assertEqual(result, expected_result)

    def test_sort_list_negative_numbers(self):
        arr = [-5, 0, 5]
        expected_result = [5, 0, -5, -5]
        result = sort_list(arr)
        self.assertEqual(result, expected_result)

    def test_sort_list_even_number_of_elements(self):
        arr = [2, 4, 6, 8]
        expected_result = [8, 4, 6, 2, 2]
        result = sort_list(arr)
        self.assertEqual(result, expected_result)

    def test_sort_list_single_element(self):
        arr = [1]
        expected_result = [1, 1]
        result = sort_list(arr)
        self.assertEqual(result, expected_result)

    def test_sort_list_multiple_identical_elements(self):
        arr = [1, 2, 1, 3]
        expected_result = [3, 2, 3, 1, 1]
        result = sort_list(arr)
        self.assertEqual(result, expected_result)
