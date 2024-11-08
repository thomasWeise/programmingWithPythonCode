"""A simple example for generator functions."""

from typing import Generator  # The type hint for generators.


def fibonacci() -> Generator[int, None, None]:
    """A generator returning Fibonacci numbers."""
    i: int = 0  # Initialize i.
    j: int = 1  # Initialize j.
    while True:  # Loop forever, i.e., generator can continue forever.
        yield i  # Return the Fibonacci number.
        i, j = j, i + j  # i = old_j and j = old_i + old_j


for a in fibonacci():  # Loop over the generated sequence.
    print(a)  # Print the sequence element.
    if a > 30:  # If a > 300, then
        break    # we stop the iteration.

# list(fibonacci()) <-- This would fail!!
