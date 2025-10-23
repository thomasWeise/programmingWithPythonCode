"""Test our function."""

from tests_01 import my_isqrt

def test_my_sqrt() -> None:
    """Test `my_sqrt`."""
    assert my_isqrt(0) == 0
    assert my_isqrt(1) == 1
    assert my_isqrt(3) == 1
    assert my_isqrt(4) == 2
    assert my_isqrt(8) == 2
    assert my_isqrt(9) == 3
    assert my_isqrt(16) == 4
