"""A simple example for generator functions."""

from typing import Generator  # The type hint for generators.


def generator_123() -> Generator[int, None, None]:
    """A generator function which yields 1, 2, 3."""
    yield 1  # The first time next(...) is called, the result is 1.
    yield 2  # The second time next(...) is called, the result is 2.
    yield 3  # The third time next(...) is called, the result is 3.

as_list: list[int] = list(generator_123())  # Create a list.
print(f"{as_list = }")  # The list is [1, 2, 3].

gen: Generator[int, None, None] = generator_123()  # Use directly.
print(f"{next(gen) = }")  # First time next: get 1.
print(f"{next(gen) = }")  # Second time next: get 2.
print(f"{next(gen) = }", flush=True)  # Third time next: get 3.
print(f"{next(gen) = }", flush=True)  # raises StopIteration
