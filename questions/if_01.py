""" If-then-else Examples. """

from math import isqrt

number = 121
if (number % 2) == 0:
    print(f"Number {number} is even.")

if number > 12:
    print(f"Number {number} is bigger than 12.")

if number == isqrt(number) ** 2:
    print("Interesting.")
