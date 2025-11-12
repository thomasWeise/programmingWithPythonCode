""" Convert a `while`-loop to a `for`-loop. """

data: list[str] = ["Hello", "World", "I", "am", "here"]

index: int = 0
while index < len(data):
    print(f"The element at index {index} is {data[index]}.")
    index += 1
