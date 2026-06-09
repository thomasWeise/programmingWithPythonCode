# This program has an error.

def largest_divisor(value: int)->int:
    largest: int = -1
    for v in range(value):
        if value % v == 0:
            largest = v
    return largest

print(largest_divisor(10))
print(largest_divisor(16))
