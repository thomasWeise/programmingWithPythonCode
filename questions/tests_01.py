"""Working with tests."""

def my_isqrt(a: int) -> int:
    """
    An implementation of the integer square root of numbers.

    :param a: an integer number
    :return: the integer square root of that number
    """
    result: int = 0
    while result * result < a:
        result += 1

    return result
