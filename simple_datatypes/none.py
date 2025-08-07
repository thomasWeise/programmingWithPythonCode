None                          # Prints nothing.
print(None)                   # Prints "None".

# The use the equality comparisons via == is discouraged if None may
# be involved. We do it here anyway, just to see what it does.
1 == None                     # False
"Hello World!" == None        # also False
# Different from 'nan == nan', which is False, 'None == None' is...
None == None                  # ...True

# It is encouraged to use 'is' instead, which checks object identity
# (not equality like ==).
1 is None                     # False
"Hello World!" is None        # False
None is None                  # True

print(print("Hello World!"))  # Prints "Hello World!" and "None".
type(None)                    # None is the only instance of NoneType
