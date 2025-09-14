x = ["a", "b", "c"]       # Create a list `x` of three strings.

>>> for xi in x:    # We can loop over this list.
...     print(xi)

>>> for xi in x:    # We can loop over this list as often as we want.
...     print(f"Hello letter {xi!r}!")

from typing import Iterable, Iterator  # Import the two iteration types.
isinstance(x, Iterable)  # Check if `x` can be iterated over.
u = iter(x)              # Create an Iterator `u` over Iterable `x`.
isinstance(u, Iterator)  # Check if `u` really is an `Iterator`.
type(u)                  # The type of `u` is a subclass of `Iterator`.
v = iter(x)              # Create an Iterator `v` over Iterable `x`.
next(u)                  # Get first element in sequence `u`: `"a"`.
next(u)                  # Get second element in sequence `u`: `"b"`.
next(v)                  # Get first element in sequence `v`: `"a"`.
next(u)                  # Get third element in sequence `u`: `"c"`.
next(u)                  # `u` is exhausted, raises `StopIteration`.
next(v)                  # Get second element in sequence `v`: `"b"`
w = iter(x)              # Create an Iterator `w` over Iterable `x`.
next(w)                  # Get first element in sequence `w`: `"a"`.
next(v)                  # Get third element in sequence `v`: `"c"`.
next(v)                  # `v` is exhausted, raises `StopIteration`.

print("Done.")
