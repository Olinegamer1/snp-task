import unittest
from task_03 import max_odd


class TestMaxOdd(unittest.TestCase):

    def test_simple_max_odd(self):
        self.assertEqual(max_odd([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_odd([1, 3, 5, 7]), 7)
        self.assertEqual(max_odd([0, 1, 2, 3]), 3)

    def test_negative_max_odd(self):
        self.assertEqual(max_odd([-1, -2, -3, -4]), -1)

    def test_empty_array(self):
        self.assertIsNone(max_odd([]))

    def test_only_evens(self):
        self.assertIsNone(max_odd([2, 4, 6, 8]))

    def test_float_numbers(self):
        self.assertEqual(max_odd([1.5, 3.5, 5.5, 4.4, 2.2]), 5.5)

    def test_with_str(self):
        self.assertEqual(max_odd([1, 2, 'foo', 3, 'bar']), 3)

    def test_only_str(self):
        self.assertIsNone(max_odd(['foo', 'bar', 'baz']))
