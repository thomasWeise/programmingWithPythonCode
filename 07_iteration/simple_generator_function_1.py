"""A simple example for generator functions."""

from typing import Generator


def generator_123() -> Generator[int, None, None]:
    """A generator function which yields 1, 2, 3."""
    yield 1
    yield 2
    yield 3

as_list: list[int] = list(generator_123())
print(f"as list: {as_list}")

gen = generator_123()
print(f"next(gen): {next(gen)}")
print(f"next(gen): {next(gen)}")
print(f"next(gen): {next(gen)}", flush=True)
print(f"next(gen): {next(gen)}", flush=True)
