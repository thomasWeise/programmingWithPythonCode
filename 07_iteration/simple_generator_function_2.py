"""A simple example for generator functions."""

from typing import Generator


def multiples_of_37() -> Generator[int, None, None]:
    """A generator yielding all multiples of 37."""
    i: int = 1
    while True:  # Loop forever, i.e., generator can continue forever.
        yield i * 37  # Yield the multiple.
        i += 1


for a in multiples_of_37():  # Loop over the generated sequence.
    print(f"a = {a}")  # Print the sequence element.
    if a > 300:  # If a > 300, then
        break    # we stop the iteration.

# list(multiples_of_37()) <-- This would fail!!
