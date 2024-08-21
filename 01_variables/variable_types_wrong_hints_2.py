float_var: float = 1 + 7  # Store an int in a variable hinted as float.
print(type(float_var))  # This prints "<class 'int'>".

float_var = float_var / 3  # / returns a float - as we would except.
print(type(float_var))  # This now prints "<class 'float'>".
