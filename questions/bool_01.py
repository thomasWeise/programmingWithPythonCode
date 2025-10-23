"""Working with Boolean expressions."""

a: bool = 1 < 5 <= 5 < 6  # Line 3
print(a)                  # Line 4: What does this print?

b: str  = "Hello World!"  # Line 6
c: bool = b is not b      # Line 7
print(c)                  # Line 8: What does this print?

print(a or c)             # Line 10: What does this print?
print(a and c)            # Line 11: What does this print?
print(c or b)             # Line 12 (BONUS): What does this print?
