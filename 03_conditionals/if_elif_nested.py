"""An example for using the nested `if-else` statements and `elif`."""

a: int = 13  # the first number
b: int = 7  # the second number
c: int = 9  # the third number

if a > b:  # This means that a > b
    if a > c:  # This means that a > b and a > c.
        print(f"{a} is the greatest number.")
    else:  # This means that a > b and c >= a.
       print(f"{c} is the greatest number.")
elif b > c:  # This means that b >= a and b > c.
    print(f"{b} is the greatest number.")
else:  # This means that b >= a and c >= b.
    print(f"{c} is the greatest number.")
