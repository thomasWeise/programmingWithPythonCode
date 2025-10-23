"""Sets in Python."""

st1: set[str] = {"a", "b", "c", "e", "e", "f", "g"}
print("a" in st1)           # Line 4: What does it print?
print("x" in st1)           # Line 5: What does it print?

st2: set[str] = {"f", "h", "x", "c", "f"}
print(st1.union(st2))       # Line 8: What could it print?
print(st1.difference(st2))  # Line 9: What could it print?
