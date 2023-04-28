from typing import List, Union


def max_odd(arr: List) -> Union[None, int, float]:
    """
    Returns max odd number in arr. If arr doesn't contain an odd number, returns None.
    """

    numbers = (num for num in arr if isinstance(num, (int, float)))
    odd_numbers = list(filter(lambda num: num % 2 != 0, numbers))

    return max(odd_numbers) if odd_numbers else None
