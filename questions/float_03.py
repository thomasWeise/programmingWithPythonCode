""" Limitations of Floating Point Numerics """

from math import pi, sin

print( 3 - sin(pi) )     # This prints 3.
print( 1 / sin(pi) )     # Then why is this "8165619676597685.0"?

print( 1e100 / 1e100 )   # This is 1.0

print( 1e400 / 1e400 )   # Then why is this "nan"?
