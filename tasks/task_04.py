from typing import List


def sort_list(arr: List) -> List:
    """
    Swap the min and max values in all cases and will add a min value at the end.
    """

    if not arr:
        return []

    min_value, max_value = min(arr), max(arr)

    if min_value == max_value:
        return arr + [min_value]

    return [swap_values(x, max_value, min_value) for x in arr] + [min_value]


def swap_values(val, max_value, min_value):
    """
    If val equals max_value then return min_value.
    Else if val equals min_value then return max_value.
    Returns val by default.
    """

    return max_value if val == min_value else min_value if val == max_value else val
