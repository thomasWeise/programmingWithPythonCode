"""Examples for using our class :class:`KahanSum`."""

from math import fsum  # An (even more) exact summation algorithm.

from kahan_sum import KahanSum

# Iterate over four example arrays.
for numbers in [[1e-15, 1e-14, 1e-13, 1e-16, 1e-12], [1e18, 1, -1e18],
                [1e36, 1e18, 1, -1e36, -1e18],
                [1e36, 1e72, 1e18, -1e36, -1e72, 1, -1e18],
                [1, -1e-16, 1e-16, 1e-16]]:
    print(f"======= numbers = [{', '.join(map(str, numbers))}] =======")
    k: KahanSum = KahanSum()  # Create our Kahan summation object.
    for n in numbers:  # Iterate over the numbers...
        k.add(n)       # ...and let our object add them up.
    print(f"sum(numbers)  = {sum(numbers)}")   # the normal sum
    print(f"Kahan sum     = {k.result()}")     # our better result
    print(f"fsum(numbers) = {fsum(numbers)}")  # the exact result
