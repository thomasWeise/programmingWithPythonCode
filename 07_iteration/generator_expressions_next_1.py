"""The iteration behavior of generator expressions and `next`."""

from typing import Generator  # Import the generator type hint.

gen: Generator[int, None, None] = (i ** 2 for i in range(1_000_000_000))
print(f"type(gen): {type(gen)}")  # Type is `generator`, not `tuple`
print(f"next(gen): {next(gen)}")  # Returns first element = 0
print(f"next(gen): {next(gen)}")  # Returns second element = 1
print(f"next(gen): {next(gen)}")  # Returns third element = 4
print(f"next(gen): {next(gen)}")  # Returns fourth element = 9
# We stop using the generator here, so the remaining 999999996 elements
# are never generated.
