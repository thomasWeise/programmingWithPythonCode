"""Testing our sqrt function that raises an error for invalid inputs."""

from math import inf, nan  # some maths constants

from pytest import raises  # Needed checking that exceptions are raised.

from sqrt_raise import sqrt  # Import our new sqrt function.


def test_sqrt() -> None:
    """Test the new `sqrt` function that raises errors."""
    assert sqrt(0.0) == 0.0  # The square root of 0 is 0.
    # ... We skip the other tests here for space reasons.

    for v in [-1.0, inf, -inf, nan]:
        with raises(ArithmeticError, match="sqrt.* is not permitted."):
            sqrt(v)  # The square root of v is not permitted
