"""Example of the built-in functions str, ceil, floor, and round."""

from math import ceil, floor

a = 0.9999999999999999999999999999999
b = 1.5
print("==== " + str(a) + " and " + str(b) + " ====")
print(round(a) - round(b))   # prints -1
print( ceil(a) - ceil(b))    # prints -1
print(floor(a) - floor(b))   # prints 0

c = 1.9999999999999999999999999999999
d = 2.5
print("==== " + str(c) + " and " + str(d) + " ====")
print(round(c) - round(d))   # prints 0
print( ceil(c) - ceil(d))    # prints -1
print(floor(c) - floor(d))   # prints 0
