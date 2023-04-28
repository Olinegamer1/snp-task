import unittest
from task_02 import coincidence


class TestCoincidence(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(coincidence(), [])

    def test_with_none_as_range_arr(self):
        self.assertEqual(coincidence([1, 2, 3], None), [])

    def test_with_none_as_arr(self):
        self.assertEqual(coincidence(None, range(1, 4)), [])

    def test_with_empty_range(self):
        self.assertEqual(coincidence([-1, 0, 1, 2, 4], range(0)), [])

    def test_with_empty_array(self):
        self.assertEqual(coincidence([], range(1, 4)), [])

    def test_with_no_coincidences_in_the_array(self):
        self.assertEqual(coincidence([1, 2, 3], range(4, 7)), [])

    def test_with_some_coincidences_in_the_array(self):
        self.assertEqual(coincidence([1, 2, 3, 4, 5, 6], range(3, 5)), [3, 4])

    def test_with_decimal_range(self):
        self.assertEqual(coincidence([1, 2, 3.5, 4, 5], range(2, 5)), [2, 3.5, 4])
