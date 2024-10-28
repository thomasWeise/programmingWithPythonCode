"""Testing our mathematical functions."""

from math import inf, nan  # some maths constants

from pytest import raises  # Needed checking that exceptions are raised.

from sqrt_raise import sqrt  # Import our new sqrt function.


def test_sqrt() -> None:
    """Test the new `sqrt` function that raises errors."""
    assert sqrt(0.0) == 0.0  # The square root of 0 is 0.
    assert sqrt(1.0) == 1.0  # The square root of 1 is 1.
    # ... We skip the other tests here for space reasons.

    with raises(ArithmeticError, match="sqrt(.*) is not permitted."):
        sqrt(-1.0)  # The square root of negative numbers is not permitted

    with raises(ArithmeticError, match="sqrt(.*) is not permitted."):
        sqrt(inf)  # The square root of `inf` is not permitted

    with raises(ArithmeticError, match="sqrt(.*) is not permitted."):
        sqrt(-inf)  # The square root of `-inf` is not permitted

    with raises(ArithmeticError, match="sqrt(.*) is not permitted."):
        sqrt(nan)  # The square root of `nan` is not permitted
