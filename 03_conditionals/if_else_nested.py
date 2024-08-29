"""An example for using the nested `if-else` statements."""

a: int = 13
b: int = 7
c: int = 9

if a > b:
    if a > c:
        print(f"{a} is the greatest number.")
    else:
        print(f"{c} is the greatest number.")
else:
    if b > c:
        print(f"{b} is the greatest number.")
    else:
        print(f"{c} is the greatest number.")
