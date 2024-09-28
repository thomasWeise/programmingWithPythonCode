"""Euclidian Algorithm for the Greatest Common Divisor as a function."""

from math import gcd as math_gcd  # use math's gcd under name `math_gcd`

def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of two numbers `a` and `b`.

    :param a: the first number
    :param b: the second number
    :return: the greatest common divisor of `a` and `b`
    """
    while b != 0:
        a, b = b, a % b
    return a


def print_gcd(a: int, b: int) -> None:
    """
    Print the result of the gcd of `a` and `b`.

    :param a: the first number
    :param b: the second number
    """
    print(f"gcd({a}, {b})={gcd(a, b)}, math_gcd={math_gcd(a, b)}.")


print_gcd(1, 0)
print_gcd(0, 1)
print_gcd(765, 273)
print_gcd(24359573700, 35943207300)
