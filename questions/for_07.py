"""Print Pascal's Triangle."""

from math import factorial
from typing import Final

n: Final[int] = 9

for i in range(n):
    print(" " * (n - i), end="")

    for j in range(i + 1):
        value = factorial(i) // (factorial(j) * factorial(i - j))
        print(f"{value:2}", end=" ")
    print()
