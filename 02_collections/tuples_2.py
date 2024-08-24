"""An example for creating tuples of mixed types."""

mixed: tuple[str, int, float] = ("apple", 12, 1e25)  # mixed types
print(f"The mixed tuple is {mixed}.")  # print the tuple

other: tuple[str, int, float] = ("pear", 1, 1.2)  # second such tuple
print(f"the other tuple: {other}.")  # print  it as well

tuples: list[tuple[str, int, float]] = [  # create a list of 4 tuples
    mixed, ("pear", -2, 4.5), other, ("pear", -2, 3.3), ]
print(f"tuples list: {tuples}.")  # print that list

tuples.sort()  # sort the list
print(f"sorted tuples list: {tuples}.")

a, b, c = mixed  # we unpack the tuple
print(f"a={a}, b={b}, c={c}")
