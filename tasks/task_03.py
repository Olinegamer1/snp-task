from typing import List


def max_odd(arr: List):
    """
    Return max odd number in arr. If arr doesn't contain an odd number, return None.
    """

    number_list = [num for num in arr if isinstance(num, (int, float))]
    odd_numbers = list(filter(lambda num: num % 2 != 0, number_list))

    if not odd_numbers:
        return None

    return max(odd_numbers)
