"""Testing our second implementation of Heron's Method."""

from math import inf, isnan, nan  # some float value-checking functions

from def_sqrt_2 import sqrt  # Get our 2nd square root implementation.


def test_sqrt() -> None:
    """Test the function `sqrt` from module `def_sqrt_2`."""
    assert sqrt(0.0) == 0.0  # The square root of 0 is 0.
    assert sqrt(1.0) == 1.0  # The square root of 1 is 1.
    assert sqrt(4.0) == 2.0  # The square root of 4 is 2.
    s3: float = sqrt(3.0)  # Get the approximated square root of 3.
    assert abs(s3 * s3 - 3.0) <= 5e-16  # sqrt(3)² should be close to 3.
    assert sqrt(10e9 * 10e9) == 10e9  # 10e9² = 10e9 * 10e9
    assert sqrt(inf) == inf  # The square root of +inf is +inf.
    assert isnan(sqrt(nan))  # The root of not-a-number is still nan.
