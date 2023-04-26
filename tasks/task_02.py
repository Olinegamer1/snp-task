from typing import List


def coincidence(arr: List = None, range_arr: range = None):
    """
     Returns a list of numbers which contained in a range range_arr.
     If one or both arguments are None, return an empty list.
    """

    if arr is None or range_arr is None:
        return []

    number_arr = tuple(num for num in arr if isinstance(num, (int, float)))
    return [num for num in number_arr if is_number_in_range(num, range_arr)]


def is_number_in_range(number: int | float, range_arr: range):
    """ Return True if number contained in a range. """

    return range_arr[0] <= number <= range_arr[-1] if tuple(range_arr) else False

