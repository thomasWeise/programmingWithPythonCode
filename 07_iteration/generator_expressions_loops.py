"""Generator expressions in `for` loops."""

from math import sin

# The generator expression produces tuples (n, sin(n)).
# The for loop iterates over the generator expression and unpacks the
# tuples into the variables o and p.
for o, p in ((n, sin(n)) for n in range(1_000_000_000)):
    if p < -0.99999:  # We look for an n with sin(n) < -0.99999.
        print(f"sin({o})={p}")  # We found it and print it.
        break  # And stop the iteration, not using the full range.
