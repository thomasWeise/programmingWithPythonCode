"""Tuples: What output is produced by this program?"""

a: tuple[int, ...] = (4, 1, 2, 3)

b, c, d, e = a
print(b)                   # Line 6: What does it print?
print(e)                   # Line 7: What does it print?

a = (c, e, d, b)
print(a)                   # Line 10: What does it print?

f: tuple[tuple[int, int], int, tuple[int, int]] = (b, b), c, (d, d)
print(f.index((2, 2)))     # Line 13: What does it print?
