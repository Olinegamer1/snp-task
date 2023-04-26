from typing import Dict
from constants import THRESHOLD


def connect_dicts(d1: Dict[str, int], d2: Dict[str, int]) -> Dict[str, int]:
    """
    The 'connect_dicts' takes two dictionaries as input and returns a new dictionary that
    combines the keys and values of both input dictionaries.
    Returns a new Dict by these rules:
            * The keys from the dictionary with a higher sum of values have a
              higher priority. If the sum of values is equal, the keys from the
              second dictionary have a higher priority.
            * Key values must be greater than THRESHOLD
            * Sorted by key values in ASC order.
    """

    sum_d1, sum_d2 = sum(d1.values()), sum(d2.values())
    priority, other = (d1, d2) if sum_d1 > sum_d2 else (d2, d1)

    res = dict(other)
    res.update(priority)

    res = filter_by_value(res, THRESHOLD)
    res = sort_by_value(res)

    return res


def sort_by_value(dictionary: Dict[str, int]) -> Dict[str, int]:
    """ Returns a new Dict, filtered and sorted in ASC order. """
    return {key: value for key, value in sorted(dictionary.items(), key=lambda item: item[1])}


def filter_by_value(dictionary: Dict[str, int], threshold: int) -> Dict[str, int]:
    """ Returns a new Dict where its values are greater than the threshold. """
    return {key: value for key, value in dictionary.items() if value > threshold}
