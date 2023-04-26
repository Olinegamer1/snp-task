from typing import Iterable


def combine_anagrams(words: Iterable[str]) -> Iterable[Iterable[str]]:
    """
    Gets a list of words and breaks them into groups by anagrams.
    The letter case does not matter.
    Returns a list of anagram lists.
    """

    anagrams: dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word] = anagrams.setdefault(sorted_word, []) + [word]

    return list(anagrams.values())
