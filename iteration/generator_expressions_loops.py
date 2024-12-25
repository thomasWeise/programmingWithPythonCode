"""Generator expressions in `for` loops."""

from math import sin
from typing import Generator

# The generator expression produces tuples (n, sin(n)).
gen: Generator[tuple[int, float], None, None] = (
    (n, sin(n)) for n in range(1_000_000_000))

# The for loop iterates over the generator expression and unpacks the
# tuples into the variables o and p.
for o, p in gen:
    if p < -0.99999:  # We look for an n with sin(n) < -0.99999.
        print(f"sin({o})={p}")  # We found it and print it.
        break  # And stop the iteration, not using the full range.
