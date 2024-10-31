"""An example of testing the immutability of tuples."""

# Create a tuple consisting of an immutable object (the integer `1`) and
# a mutable object (the list [2]).
mt: tuple[int, list[int]] = (1, [2])
print(f"mt == {mt}")  # This prints mt == (1, [2])

mt[1].append(2)  # We can actually change the list inside the tuple.
print(f"mt == {mt}")  # This prints mt == (1, [2, 2])

mt[1] = [3, 4]  # However, this will fail with an TypeError exception.
print(f"mt == {mt}")  # ...and we never reach this part.
