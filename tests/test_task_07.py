import unittest
from task_07 import combine_anagrams


class TestCombineAnagrams(unittest.TestCase):

    def test_combine_anagrams_normal_case(self):
        words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
        expected_output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertEqual(combine_anagrams(words), expected_output)

    def test_combine_anagrams_empty_list(self):
        words = []
        expected_output = []
        self.assertEqual(combine_anagrams(words), expected_output)

    def test_combine_anagrams_two_words_in_list(self):
        words = ['hello', 'world']
        expected_output = [['hello'], ['world']]
        self.assertEqual(combine_anagrams(words), expected_output)

    def test_combine_anagrams_all_same_words(self):
        words = ['abc', 'abc', 'abc', 'abc', 'abc', 'abc']
        expected_output = [['abc', 'abc', 'abc', 'abc', 'abc', 'abc']]
        self.assertEqual(combine_anagrams(words), expected_output)

    def test_combine_anagrams_different_lengths_and_cases(self):
        words = ['Abcdefg', 'gfEdcba', 'abc', 'cba', 'defg', 'gfed']
        expected_output = [['Abcdefg', 'gfEdcba'], ['abc', 'cba'], ['defg', 'gfed']]
        self.assertEqual(combine_anagrams(words), expected_output)

        words = ['race', 'Care', 'acre', 'dog', 'god']
        expected_output = [['race', 'Care', 'acre'], ['dog', 'god']]
        self.assertEqual(combine_anagrams(words), expected_output)
