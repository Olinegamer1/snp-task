import unittest
from tasks.task_08 import multiply_numbers


class TestMultiplyNumbers(unittest.TestCase):

    def test_none_input(self):
        self.assertIsNone(multiply_numbers())
        self.assertIsNone(multiply_numbers('ss'))

    def test_valid_input(self):
        self.assertEqual(multiply_numbers('1234'), 24)
        self.assertEqual(multiply_numbers('sssdd34'), 12)
        self.assertEqual(multiply_numbers(2.3), 6)
        self.assertEqual(multiply_numbers([5, 6, 4]), 120)
        self.assertEqual(multiply_numbers((1, 2, 3, 4, 5, 6, 7, 8, 9)), 362880)
        self.assertEqual(multiply_numbers({1, 2, 3, 4, 5, 6, 7, 8, 9}), 362880)
