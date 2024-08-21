int_var: int = 1 + 7  # Create a variable hinted as integer.
print(type(int_var))  # This prints "<class 'int'>".

int_var = int_var / 3  # / returns a float, but we may expect an int?
print(type(int_var))  # This now prints "<class 'float'>".
