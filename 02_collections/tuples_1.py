"""An example of creating, indexing, and printing tuples."""

fruits: tuple[str, str, str] = ("apple", "pear", "orange")
print(f"We got {len(fruits)} fruits: {fruits}")

veggies: tuple[str, ...] = ("onion", "potato", "leek", "garlic")
print(f"The vegetables are: {veggies}.")  # Print the tuple.

print(f"{veggies[0] = }")  # first element of `veggies`.
print(f"{veggies[1] = }")  # second element of `veggies`.
print(f"{veggies[-1] = }")  # last element of `veggies`.
print(f"{veggies[-2] = }")  # second-to-last element.

print(f"is pear in fruits: {'pear' in fruits}")
print(f"is pear in veggies: {'pear' in veggies}")
print(f"apple is at index {fruits.index('apple')} in fruits.")
