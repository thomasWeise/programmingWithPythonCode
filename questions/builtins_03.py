"""Example of the built-ins sin, asin, cos, acos, and pi."""

from math import sin, cos, asin, acos, pi

print(sin(0))                  # prints 0.0
print(sin(0.5 * pi))           # prints 1.0
print(asin(1))                 # prints 1.5707963267948966
print(sin(pi / 4))             # prints 0.7071067811865475
print((1 / sin(pi / 4)) ** 2)  # prints 2.0000000000000004

print(cos(0))                  # prints 1.0
print(cos(pi / 3))             # prints 0.5000000000000001
print(acos(0.5))               # prints 1.0471975511965979
