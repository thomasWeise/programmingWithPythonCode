"""A generator function for prime numbers."""

from math import isqrt
from typing import Generator


def primes() -> Generator[int, None, None]:
    """
    Provide a sequence of prime numbers.

    >>> gen = primes()
    >>> next(gen)
    2
    >>> next(gen)
    3
    >>> next(gen)
    5
    >>> next(gen)
    7
    >>> next(gen)
    11
    """
    yield 2

    found: list[int] = []  # The list of already discovered primes.
    candidate: int = 1  # The current prime candidate
    while True:  # Loop over candidates.
        candidate += 2  # Move to the next odd number as prime candidate
        is_prime: bool = True  # Let us assume that `candidate` is prime.
        limit: int = isqrt(candidate)  # Get the maximum possible divisor.
        for check in found:  # We only test with the odd primes we got.
            if check > limit:  # If the potential divisor is too big, then
                break          # we can stop the inner loop here.
            if candidate % check == 0:  # modulo == 0: division without rest
                is_prime = False  # If check divides candidate evenly, then
                break  # candidate is not a prime. We can stop the inner loop.

        if is_prime:  # If True: no smaller number divides candidate evenly.
            yield candidate  # Return the prime number as next element.
            found.append(candidate)  # Store candidate in primes list.
