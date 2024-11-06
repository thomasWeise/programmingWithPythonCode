"""Try to measure the performance of list comprehension."""

from timeit import timeit  # needed for measuring the runtime


def create_by_comprehension() -> list[int]:
    """
    Create the list of even numbers within 0..1'000'000.

    :return: the list of even numbers within 0..1'000'000
    """
    return [i for i in range(1_000_001) if i % 2 == 0]


# Measure how long 10 executions of create_by_comprehension take in seconds,
# then divide by 10 to get the time per execution.
time_in_s: float = timeit(create_by_comprehension, number=10) / 10
print(f"time in s: {time_in_s}")  # Print the result.
