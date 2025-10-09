int("1111")        # Convert decimal number 1111 to int.
int("0x1111", 16)  # Convert hexadecimal number 1111 to int.
int("0b1111", 2)   # Convert binary number 1111 to int.

float("2.233e4")   # fractional number in scientific notation and
float("0.1123")    # normal fractional number converted to float
float("inf")       # convert to float value inf
float("nan")       # convert to float value not-a-number

# bool works differently!
# It performs a standard truth test, which returns `False` if its
# argument is False, 0, and empty string or sequence, or None.
# Otherwise, it returns True.
# So it is actually True for the string "False".
# "" is an empty string, but "False" is not an empty string....
bool("True")       # convert to the bool value True
bool("False")      # convert to the bool value True!!
bool("")           # convert to the bool value False
