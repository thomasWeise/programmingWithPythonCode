# NEVER NEVER NEVER EVER DO THIS.

import math                  # Let's grab the math module.
from math import sin

print(math.pi)               # This prints 3.141592653589793
print(sin(math.pi))          # 1.2246467991473532e-16, so basically 0.

math.pi = 3                  # We change the value of the variable pi.
print(math.pi)               # This now prints 3.

from math import pi          # And import the variable into our scope.
print(math.sin(pi))          # We changed the variable pi, but the
                             # mathematical constant is still the same.
                             # So here we get 0.1411200080598672.

math.nan = 5                 # Now the variable "nan" becomes 5, but 5 is
                             # still a number, i.e., not a (not a number)!
print(math.isnan(math.nan))  # Therefore, this prints False.

math.inf = 10000             # 10000 is fairly large, right?
from math import inf         # Let's get the value `inf` into our scope.
print(50000 > inf)           # This now prints True.
