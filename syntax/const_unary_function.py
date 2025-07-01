# The syntax of a unary function always returning a constance value.
def const_1(x: float) -> float:
    return 1.0   # always return 1.0, regardless of the value of x

# or

# It is common to use "_" as name for parameters that we will ignore.
def const_1(_: float) -> float:
    return 1.0   # always return 1.0, parameter "_" is ignored.
