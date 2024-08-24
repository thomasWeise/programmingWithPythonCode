"""An example for more operations with lists."""

l1: list[int] = [1, 2, 3, 4]  # create first list
l2: list[int] = [5, 6, 7]  # create second list
l3: list[int] = l1 + l2  # l3 = concatenation of l1 and l2.
print(f"l3 = l1 + l2 == {l3}")  # [1, 2, 3, 4, 5, 6, 7]

l4: list[int] = l2 * 3  # l4 = l2, repeated three times.
print(f"l4 = l2 * 3 == {l4}")  # [5, 6, 7, 5, 6, 7, 5, 6, 7]

l5: list[int] = l4[2:-2]  # l5 = l4 from index 2 to 3rd from end
print(f"l5 = l4[2:-2] == {l5}")  # [7, 5, 6, 7, 5]

l6: list[int] = l4[1::2]  # start at index 1, take every 2nd element
print(f"l6 = l4[1::2] == {l6}")  # [6, 5, 7, 6]

# Start copying l4 at last element, move backwards take every 3rd
# element, and stop right before index=2.
l7: list[int] = l4[-1:2:-3]
print(f"l7 = l4[-1:2:-3] == {l7}")  # [7, 7]

a, b, c = l2  # store the three elements of l2 into variables
print(f"a={a}, b={b}, c={c}")  # a=5, b=6, c=7
