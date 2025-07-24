round(0.4)  # `round` performs Banker's rounding: It rounds to the
round(0.5)  # closest whole number. If two numbers are equally far
round(0.6)  # from its argument, `round` returns the *even* number.
round(1.4)  # So 1.5 gets rounded to 2, but 0.5 gets rounded to 0.
round(1.5)

from math import floor, trunc, ceil
floor(0.4)   # `floor` rounds towards negative infinity. If its
floor(0.5)   # has a fractional part, it always gets rounded down.
floor(0.6)   # Thus, 0.6 becomes 0 and -0.4 becomes -1.
floor(-0.4)  # The opposite of `floor` is `ceil`.

trunc(0.4)   # `trunc` cuts off the fractional part of a number.
trunc(0.6)   # Thus, 0.6 becomes 0 and -0.6 becomes 0, too.
trunc(-0.4)  # 10.9 would become 10, if we tried to compute that,
trunc(-0.6)  # and -10.9 would become -10.

ceil(0.4)    # `ceil` is the opposite of `floor`: It rounds toward
ceil(-11.1)  # positive infinity. Therefore, 0.4 becomes 1 and -11.6
ceil(-11.6)  # becomes -11.
ceil(11.6)

trunc(11.6)  # One stray `trunc` example: 11.6 becomes 11.

int(0.9)     # `int` works exactly like `trunc`. There only is a
int(-0.9)    # semantic difference: `int` it a type conversion
int(11.6)    # operation and `trunc` is a mathematical operator.

int(11.5 + 0.5)  # "Rounding up numbers of the form "x.5y" can be
int(12.5 + 0.5)  # achieved via `int(x + 0.5)`.
