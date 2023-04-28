import unittest
from task_10 import counts_word


class TestCountsWord(unittest.TestCase):

    def test_counts_word_hello_world(self):
        self.assertEqual(counts_word('Hello world!'), {'hello': 1, 'world': 1})

    def test_counts_word_test_sentence(self):
        self.assertEqual(counts_word('this is a test sentence. this sentence is for testing.'),
                         {'this': 2, 'is': 2, 'a': 1, 'test': 1, 'sentence': 2, 'for': 1, 'testing': 1})

    def test_counts_word_multiple_repeated_words(self):
        self.assertEqual(counts_word('a a a b b c c c c'), {'a': 3, 'b': 2, 'c': 4})

    def test_counts_word_empty_string(self):
        self.assertEqual(counts_word(''), {})

    def test_counts_word_multiple_empty_strings(self):
        self.assertEqual(counts_word(''   ''), {})

    def test_counts_word_uppercase_letters(self):
        self.assertEqual(counts_word('aAa bBb cCc'), {'aaa': 1, 'bbb': 1, 'ccc': 1})

    def test_counts_word_punctuation_and_whitespace(self):
        self.assertEqual(counts_word('Doo bee doo bee doo'), {'doo': 3, 'bee': 2})

    def test_counts_word_palindrome(self):
        self.assertEqual(counts_word('A man, a plan, a canal -- Panama'),
                         {'a': 3, 'man': 1, 'canal': 1, 'panama': 1, 'plan': 1})

    def test_counts_word_hyphenated_words(self):
        self.assertEqual(counts_word('-fast-time- is a good time!'),
                         {'fast-time': 1, 'is': 1, 'a': 1, 'good': 1, 'time': 1})
