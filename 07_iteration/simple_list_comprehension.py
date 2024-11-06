"""Simple examples for list comprehension."""

squares_1: list[int] = []  # We can start with an empty list.
for i in range(11):  # Then we use a for-loop over the numbers 0 to 10.
    squares_1.append(i ** 2)  # And append the squares to the list.

print(f" result of construction: {squares_1}")  # Print the result.

# Or we use list comprehension as follows:
squares_2: list[int] = [j ** 2 for j in range(11)]
print(f"result of comprehension: {squares_1}")  # Print the result.

even_numbers: list[int] = [k for k in range(10) if k % 2 == 0]
print(f"even numbers {even_numbers}")

combinations: list[str] = [f"{a}{b}" for a in "abc" for b in "xy"]
print(f"letter combinations: {combinations}")
