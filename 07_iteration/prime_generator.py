"""A generator function for prime numbers."""

from math import isqrt
from typing import Generator


def primes(maximum: int) -> Generator[int, None, None]:
    """
    Provide a sequence of prime numbers.

    :param maximum: the maximum number to consider.
    :return: the sequence of prime numbers `<= maximum`.

    >>> list(primes(1))
    []
    >>> list(primes(2))
    [2]
    >>> list(primes(3))
    [2, 3]
    >>> list(primes(39))
    [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39]
    """
    if maximum <= 1:
        return  # No prime <= 1.
    yield 2  # Maximum must be >= 2, so we return `2` as first element.
    if maximum <= 2:  # Is the maximum already == 2?
        return  # No further prime in this case.

    found: list[int] = []  # The list of already discovered primes.
    for candidate in range(3, maximum + 1, 2):  # Loop over candidates.
        is_prime: bool = True  # Let us assume that `candidate` is prime.
        limit: int = isqrt(candidate)  # Get the maximum possible divisor.
        for check in found[1:]:  # We only test with the odd primes we got.
            if check > limit:  # If the potential divisor is too big, then
                break          # we can stop the inner loop here.
            if candidate % check == 0:  # modulo == 0: division without rest
                is_prime = False  # If check divides candidate evenly, then
                break  # candidate is not a prime. We can stop the inner loop.

        if is_prime:  # If True: no smaller number divides candidate evenly.
            yield candidate  # Return the prime number as next element.
            found.append(candidate)  # Store candidate in primes list.
