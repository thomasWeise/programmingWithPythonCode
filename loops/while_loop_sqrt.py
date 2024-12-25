"""Using a `while` loop to implement Heron's Method."""

from math import sqrt  # math.sqrt is as exact with float as possible.

for number in [0.5, 2.0, 3.0]:  # The three numbers we want to test.
    guess: float = 1.0  # This will hold the current guess.
    old_guess: float = 0.0  # 0.0 is just a dummy value != guess.

    while old_guess != guess:  # Repeat until nothing changes anymore.
        old_guess = guess  # The current guess becomes the old guess.
        guess = 0.5 * (guess + number / guess)  # The new guess.

    actual: float = sqrt(number)  # The "actual" computed sqrt value.
    print(f"\u221A{number}\u2248{guess}, sqrt({number})={actual}")
