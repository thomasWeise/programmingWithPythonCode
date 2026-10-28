"""Conversion of strings to bools."""

print(str(True))                  # Line 3
print(bool("True"))               # Line 4

print(str(False))                 # Line 6
print(bool("False"))              # Line 7

print(bool(str(True))  == True)   # Line 9
print(bool(str(False)) == False)  # Line 10

print(bool(""))                   # Line 11
