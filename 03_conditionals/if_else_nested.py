"""An example for using the nested `if-else` statements."""

a: int = 13  # the first number
b: int = 7  # the second number
c: int = 9  # the third number

if a > b:
    if a > c:  # This means that a > b and a > c.
        print(f"{a} is the greatest number.")
    else:  # This means that a > b and c >= a.
        print(f"{c} is the greatest number.")
else:  # This means that b >= a.
    if b > c:  # This means that b >= a and b > c.
        print(f"{b} is the greatest number.")
    else:  # This means that b >= a and c >= b.
        print(f"{c} is the greatest number.")

# Some little side information:
print(f"the maximum is {max(a, b, c)}.")  # max: get maximum of a sequence
print(f"the minimum is {min(a, b, c)}.")  # min: get minimum of a sequence
