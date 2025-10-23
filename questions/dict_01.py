"""Lists: What output is produced by this program?"""

from math import sqrt

roots: dict[int, float] = {2: sqrt(2), 3: sqrt(3), 4: sqrt(4)}

print(3 in roots)           # Line 7: What does it print?
print(5 in roots)           # Line 8: What does it print?

print(roots[4])             # Line 10: What does it print?

roots[9] = sqrt(9)
del roots[2]
print(max(roots.values()))  # Line 14: What does it print?
