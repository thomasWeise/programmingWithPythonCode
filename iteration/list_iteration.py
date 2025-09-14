x = ["a", "b", "c"]
>>> for xi in x:
...     print(xi)
>>> for xi in x:
...     print(f"Hello letter {xi!r}!")
from typing import Iterable, Iterator
isinstance(x, Iterable)
u = iter(x)
isinstance(u, Iterator)
type(u)
v = iter(x)
next(u)
next(u)
next(v)
next(u)
next(u)
next(v)
w = iter(x)
next(w)
next(v)
next(v)
