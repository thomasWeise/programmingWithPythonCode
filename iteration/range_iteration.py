x = range(3)        # Create a range `x` with the numbers from 0 to 2.

>>> for xi in x:    # We can loop over this range.
...     print(xi)

>>> for xi in x:    # We can loop over this range as often as we want.
...     print(f"Hello number {xi}!")

from typing import Iterable, Iterator  # Import the two iteration types.
isinstance(x, Iterable)  # Check if `x` can be iterated over.
u = iter(x)              # Create an Iterator `u` over Iterable `x`.
isinstance(u, Iterator)  # Check if `u` really is an `Iterator`.
type(u)                  # The type of `u` is a subclass of `Iterator`.
v = iter(x)              # Create an Iterator `v` over Iterable `x`.
next(u)                  # Get first element in sequence `u`: `"0"`.
next(u)                  # Get second element in sequence `u`: `"1"`.
next(v)                  # Get first element in sequence `v`: `"0"`.
next(u)                  # Get third element in sequence `u`: `"2"`.
next(u)                  # `u` is exhausted, raises `StopIteration`.
next(v)                  # Get second element in sequence `v`: `"1"`
w = iter(x)              # Create an Iterator `w` over Iterable `x`.
next(w)                  # Get first element in sequence `w`: `"0"`.
next(v)                  # Get third element in sequence `v`: `"2"`.
next(v)                  # `v` is exhausted, raises `StopIteration`.

print("Done.")
