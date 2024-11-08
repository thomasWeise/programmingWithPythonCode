"""The iteration behavior of generator expressions and `next`."""

from typing import Generator

gen_1: Generator[int, None, None] = (i ** 2 for i in range(1_000_000_000))
print(f"type(gen_1): {type(gen_1)}")  # Type is `generator`, not `tuple`
print(f"next(gen_1): {next(gen_1)}")  # Returns first element = 0
print(f"next(gen_1): {next(gen_1)}")  # Returns first element = 1
print(f"next(gen_1): {next(gen_1)}")  # Returns first element = 4


def letter(a: int) -> str:
    """
    A simple function printing `a` and returning a letter.

    :param a: the input number
    :return: the output

    >>> letter(5)
    input is 5
    'f'
    """
    print(f"input is {a}")  # Will show that generator is lazy-evaluated
    return "abcdefgh"[a % 8]  # Return one of 8 letters.


gen_2: Generator[str, None, None] = (letter(j) for j in range(4))
print(f"type(gen_2): {type(gen_2)}")  # Again: `generator`, not `tuple`
print(f"next(gen_2): {next(gen_2)}")  # Prints input, then prints `"a"`
print(f"next(gen_2): {next(gen_2)}")  # Prints input, then prints `"b"`
print(f"next(gen_2): {next(gen_2)}")  # Prints input, then prints `"c"`
print(f"next(gen_2): {next(gen_2)}", flush=True)  # Last print
print(f"next(gen_2): {next(gen_2)}", flush=True)  # Raises StopIteration
