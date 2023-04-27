import unittest
from tasks.task_01 import is_palindrome


class TestIsPalindrome(unittest.TestCase):

    def test_palindrome_strings(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('A man a plan a canal Panama!'))
        self.assertTrue(is_palindrome('Was it a car or a cat I saw?'))

    def test_non_palindrome_strings(self):
        self.assertFalse(is_palindrome('hello world'))
        self.assertFalse(is_palindrome('Python'))
        self.assertFalse(is_palindrome('not a palindrome'))

    def test_palindrome_numbers(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(1221))
        self.assertTrue(is_palindrome(12321))

    def test_non_palindrome_numbers(self):
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(1234))

    def test_edge_cases(self):
        self.assertTrue(is_palindrome(''))
        self.assertFalse(is_palindrome(None))
        self.assertTrue(is_palindrome([]))
        self.assertTrue(is_palindrome({}))
        self.assertFalse(is_palindrome(1.23))
        self.assertFalse(is_palindrome(True))
