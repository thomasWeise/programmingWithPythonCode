"""Demonstrate `try...except` with multiple exceptions and NameError."""
from decimal import DivisionByZero

from sqrt_raise import sqrt  # Import our sqrt function.

sqrt_of_1_div_0: float

try:  # If this block raises an error, we continue at `except`.
   sqrt_of_1_div_0 = sqrt(1 / 0)  # Which error will this produce?
except DivisionByZero as de:  # A division by zero?
    print(f"We got a division-by-zero error: {de}.", flush=True)
except ArithmeticError as ae:  # Or an ArithmeticError?
    print(f"We got an arithmetic error: {ae}.", flush=True)

print(sqrt_of_1_div_0)  # Does not work: sqrt_of_1_div_0 is not assigned
print("The program is now finished.")  # We never get here.
