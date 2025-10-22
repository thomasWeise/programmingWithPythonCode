"""Working with Boolean expressions."""

a: bool = 1 < 5 <= 5 < 6
print(a)        # What does this print?

b: str  = "Hello World!"
c: bool = b is not b
print(c)        # What does this print?

print(a or c)   # What does this print?
print(a and c)  # What does this print?
print(c or b)   # What does this print? --- BONUS: gets 2 more points
