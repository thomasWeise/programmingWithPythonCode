None                          # Prints nothing.
print(None)                   # Prints "None".
1 is None                     # False
"Hello World!" is None        # also False

# Different from 'nan == nan', which is False, 'None == None' is
# True. However, using '==' is discouraged if 'None' is involved.
None == None

# It is encouraged to use 'is' instead, which checks object identity
# (not equality like ==).
None is None

print(print("Hello World!"))  # Prints "Hello World!" and "None".
type(None)                    # None is the only instance of NoneType
