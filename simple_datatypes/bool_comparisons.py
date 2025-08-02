# Compare a number to itself.
6 >  6
6 >= 6
6 == 6
6 <= 6
6 <  6
6 != 6
# Compare a smaller to a larger number.
5 >  6
5 >= 6
5 == 6
5 <= 6
5 <  6
5 != 6
# Compare a larger to a smaller number.
6 >  5
6 >= 5
6 == 5
6 <= 5
6 <  5
6 != 5

5.5 == 5  # compare a float value with an int: False due to ".5"
5.0 == 5  # compare the float 5.0 with the int 5: True!

3 <  4 < 5 <  6  # Chained comparison: True, all comparisons hold.
5 >= 4 > 4 >= 3  # Chained comparison: False, as 4 is not ">" 4.

type(True)     # type(x) returns the datatype of x.
type(5 == 5)   # type(5 == 5) is the same as type(True), i.e., bool.
