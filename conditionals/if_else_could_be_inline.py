"""An example of if-elif-else expressions that could be inlined."""

number: int = 100  # the number

# Numbers with an absolute value less than ten are small.
# If their absolute value is larger than ten, they are large.
size: str
if abs(number) < 10:  # just a random threshold for this example...
    size = "small"
else:
    size = "large"

# Numbers can be positive, negative, or unsigned (0 is unsigned).
sign: str
if number < 0:
    sign = "negative"
elif number > 0:
    sign = "positive"
else:
    sign = "unsigned"

print(f"The number {number} is {size} and {sign}.")  # Print the result.
