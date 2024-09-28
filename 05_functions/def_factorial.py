"""Implementing the factorial as a function."""

def factorial(a: int) -> int:
    """
    Compute the factorial of a positive integer `a`.

    :param a: the number to compute the factorial of
    :return: the factorial of `a`, i.e., `a!`.
    """
    prod: int = 1
    for i in range(2, a + 1):
        prod *= i
    return prod

for j in range(10):
    print(f"The factorial of {j} is {factorial(j)}.")
