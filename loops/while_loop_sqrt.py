"""Using a `while` loop to implement Heron's Method."""

from math import sqrt  # math.sqrt is as exact with float as possible.

for number in [0.5, 2.0, 3.0]:  # The three numbers we want to test.
    # Apply Heron's method to get square root of `number`.
    guess: float = 1.0          # This will hold the current guess.
    old_guess: float = 0.0      # 0.0 is just a dummy value != guess.

    while old_guess != guess:   # Repeat until nothing changes anymore.
        old_guess = guess     # The current guess becomes the old guess.
        guess = 0.5 * (guess + number / guess)  # Compute the new guess.

    actual: float = sqrt(number)  # Use the `sqrt` function from `math`.
    print(f"\u221A{number}\u2248{guess}, sqrt({number})={actual}")

# It is very bad to use `==` or `!=` as loop conditions for floating
# point numbers. As you know, floating point numbers have limited
# precession and this can cause endless loops. However, in this special
# case here, it does work. Still, never try this at home.
