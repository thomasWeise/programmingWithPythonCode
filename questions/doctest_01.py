""" An example of a function. """

from math import sqrt

def solve(a: float, b: float, c: float) -> tuple[float, float] | float:
    """
    Solve the quadratic equation `0=a*x²+b*x+c`.

    We use the formula `x = (-b +/- sqrt(b² - 4ac))/(2a)`.
    Due to the `+/-`, there are two solutions if `sqrt(b² - 4ac) != 0`.

    :param a: the coefficient `a`: We have `a*x²`.
    :param b: the coefficient `b`: We have `+b*x`.
    :param c: the coefficient `c`: We have `+c`.
    :return: either a tuple of two solutions or a single solution.

    >>> solve(2.0, -4.0, 2.0)
    1.0
    >>> solve(2.0, 0.0, -8.0)
    (-2.0, 2.0)
    >>> solve(2.0, -8.0, 6.0)
    (1.0, 3.0)
    """
    term = sqrt(b ** 2 - 4 * a * c)
    if term == 0.0:          # Check if there is only 1 solution.
        return -b / (2 * a)  # There is only 1 solution.
    return (-b - term) /(2*a), (-b * term) /(2*a)  # Return 2 solutions.
