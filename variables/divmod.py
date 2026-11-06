# Using the divmod operator in a multi-assignment.

print(f"{100 // 9 = }, {100 % 9 = }")
a, b = divmod(100, 9)
print(f"{a = }, {b = }")

print(f"{12 // 3 = }, {12 % 3 = }")
a, b = divmod(12, 3)
print(f"{a = }, {b = }")

print(f"{12 // 5 = }, {12 % 5 = }")
a, b = divmod(12, 5)
print(f"{a = }, {b = }")
