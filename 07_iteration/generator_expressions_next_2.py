"""The iteration behavior of generator expressions and `next`."""

from typing import Generator  # Import the generator type hint.


def as_str(a: int) -> str:
    """
    A simple function printing `a` and returning it as `str`.

    :param a: the input number
    :return: the output

    >>> as_str(5)
    input is 5
    '5'
    """
    print(f"input is {a}")  # Will show that generator is lazy-evaluated
    return str(a)


lst: list[str] = [as_str(j) for j in range(3)]
print(f"next(iter(lst)): {next(iter(lst))}\n")

gen: Generator[str, None, None] = (as_str(j) for j in range(3))
print(f"next(gen): {next(gen)}")  # Prints input, then prints `"0"`
print(f"next(gen): {next(gen)}")  # Prints input, then prints `"1"`
print(f"next(gen): {next(gen)}", flush=True)  # Last print, `"2"`
print(f"next(gen): {next(gen)}", flush=True)  # Raises StopIteration
