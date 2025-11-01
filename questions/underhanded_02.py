"""
Underhanded Python.

Find arguments `lower` and `upper` for which the function `all_squares`
never returns.
"""
from math import isqrt


def all_squares(lower: int, upper: int) -> list[int]:
    """
    Compute the list of all square numbers in `[lower,upper)`.

    :param lower: the lower (inclusive) interval end
    :param upper: the upper (exclusive) interval end
    :return: the list of all square numbers `s` with
        `lower <= s < upper`.

    >>> all_squares(1, 20)
    [1, 4, 9, 16]
    >>> all_squares(10, 36)  # 36 is not included: exclusive upper end!
    [16, 25]
    >>> all_squares(10, 10)
    []
    """
    # Perform a sanity check of the interval boundaries:
    # Negative lower limits are forbidden and so are large upper limits.
    if (lower <= 0) or (upper > 1_000_000) or (not isinstance(
            lower, int)) or (not isinstance(upper, int)):
        raise ValueError("Illegal Arguments!")

    result: list[int] = []  # Start with empty list.
    while lower != upper:   # We use `lower` as the variable to iterate.
        if (isqrt(lower) ** 2) == lower:  # Check if lower is a square.
            result.append(lower)  # It is! Add it to the list.
        lower += 1          # Increment lower.
    return result           # Return the list of all the square numbers.
