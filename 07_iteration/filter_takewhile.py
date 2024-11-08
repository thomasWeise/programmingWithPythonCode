"""Examples for `takewhile` and filter."""

from itertools import takewhile
from math import isqrt

from prime_generator import primes


def sqr_plus_1(x: int) -> bool:
    """
    Check whether `x` is of the form `y²+1`.

    :param x: the number to check
    :return: `True` if there is an integer `y` such that `x=y²+1`.
    """
    y: int = isqrt(x)
    return x == (y ** 2) + 1

less_than_50: list[int] = list(takewhile(lambda z: z < 50, primes()))
print(f"primes less than 50: {less_than_50}")

sqrs_plus_1: list[int] = list(filter(sqr_plus_1, takewhile(
    lambda z: z < 1000, primes())))
print(f"primes less than 1000 and of the form x²+1: {sqrs_plus_1}")
