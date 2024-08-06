# We define sqrt_2 to be a constant with the value of square root of 2.
sqrt_2 = 1.4142135623730951  # We set the value of the variable.
print(f"sqrt_2 = {sqrt_2}")  # We print the value of the variable

# We can also compute the square root using the `sqrt` function.
from math import sqrt  # Import the root function from the math module.
sqrt_2_computed = sqrt(2.0)  # Compute the square root of 2.0.
print(f"sqrt_2_computed = {sqrt_2_computed}")  # Print the value.

# Let's compare the computed and the constant value:
print(f"are they equal: {sqrt_2 == sqrt_2_computed}")
print(f"are they the same object: {sqrt_2 is sqrt_2_computed}")
