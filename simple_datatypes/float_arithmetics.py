6 / 3         # Floating-point division 6 / 3 = 2.0
1.0 + 7       # float + int = float
5 - 3.6       # int - float = float
2 * 3.0       # int * float = float
6.5 % 2       # float % int = float
3.3 ** 0.5    # square root of 3.3
((3.4 * 5.5) - 1.2) ** (4.4 / 3.3)

from math import pi, e   # import some mathematical constants
pi
e             # Euler's Number

# 0.1 cannot be exactly represented in binary float notation.
# Therefore, the sum of ten '0.1's does not add up to 1.0.
0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
# The difference is small, but it is there.
0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 - 1.0

from math import sin, cos, tan, log  # trigonometric operators
sin(0.25 * pi) ** 2   # This gives almost 0.5.
cos(pi / 3)           # This gives almost 0.5, too.
tan(pi / 4)           # And this is almost 1.
log(e ** 10)          # Sometimes, we get exact results, though.

from math import asin, acos, atan    # inverse trigonometric ops
asin(sin(0.925))      # Often, we cannot exactly invert operations.
acos(cos(-0.3))
atan(tan(1))
