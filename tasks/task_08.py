from typing import Any
from functools import reduce
from operator import mul


def multiply_numbers(inputs: Any = None) -> int | None:
    """ Return the result of multiplying of digits if they are contained in inputs. """

    numbers = tuple(parse_to_numbers(inputs))
    return reduce(mul, numbers, 1) if numbers else None


def parse_to_numbers(inputs: Any = None) -> map:
    """ Returns a map generator that includes digits. """

    return map(int, filter(str.isdigit, str(inputs)))
