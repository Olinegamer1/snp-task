from re import findall
from collections import Counter
from typing import Dict


def counts_word(string: str) -> Dict[str, int]:
    """ Returns a dictionary with the count of each word in the input string. """

    words = findall(r'\b[a-z]+[a-z-]*\b', string.lower())
    return dict(Counter(words))
