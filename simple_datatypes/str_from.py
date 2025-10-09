# Here are some functions can be used to convert strings to other types.

int("1111")        # Convert decimal number 1111 to int.
int("0x1111", 16)  # Convert hexadecimal number 1111 to int.
int("0b1111", 2)   # Convert binary number 1111 to int.

float("2.233e4")   # fractional number in scientific notation and
float("0.1123")    # normal fractional number converted to float
float("inf")       # converted to the float value for infinity
float("nan")       # converted to the float value not-a-number

# ----> WARNING: The function `bool` works differently! <----
# It performs a standard truth test, which returns `False` if its
# argument is False, 0, and empty string or sequence, or None.
# Otherwise, it returns True.
# So it is actually True for the string "False".
# "" is an empty string, but "False" is not an empty string....
bool("True")       # "True" is converted to the bool value True.
bool("False")      # "False" is converted to the bool value True!!!
bool("")           # The empty string is converts to False.
bool("blabla")     # Actually, any non-empty string becomes True.

# We now have learned how to use these functions with string parameters.
# However, they also work with parameters of other types.
# You can, for example, also do `float(1)` or `int(3.5)`.
