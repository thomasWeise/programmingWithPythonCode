"""An example of using the nested `if-else` statements."""

a: int = 13  # the first number
b: int = 7  # the second number
c: int = 9  # the third number

if a > b:      # This means that a > b
    if a > c:  # This means that a > b and a > c.
        print(f"{a} is the greatest number.")
    else:      # This means that a > b and c >= a.
        print(f"{c} is the greatest number.")
else:          # This means that b >= a.
    if b > c:  # This means that b >= a and b > c.
        print(f"{b} is the greatest number.")
    else:      # This means that b >= a and c >= b.
        print(f"{c} is the greatest number.")

# Some side information: The max and min function are very useful.
print(f"The maximum is {max(a, b, c)}.")  # max: get maximum of a sequence
print(f"The minimum is {min(a, b, c)}.")  # min: get minimum of a sequence
