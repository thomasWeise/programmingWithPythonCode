# This program has an error.

def is_prime(value: int) -> bool:
    for v in range(value):
        if value % v == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))
