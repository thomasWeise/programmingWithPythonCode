# Compare a relatively small integer to a float.
10 ** 20 == 1.0e20  # This gives us True.
10 ** 20 == 1.1e20  # This gives us False.

# Compare a larger integer to a float.
10 ** 300 == 1e300  # This, interestingly, yields False.
# The reason is the limited precision of floats of 15 to 16 digits.
int(1e300)  # Only 16 zeros are effectively there in this float.

# This must be False, because 1e400 is effectively inf.
10 ** 400 == 1e400
1e400  # <-- This prints "inf"

# In the above comparison, neither is the left-hand integer is
# converted to a float, because:
float(10 ** 400)

# Not was the right-hand float converted to an int, because:
int(1e400)
