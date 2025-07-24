1.7976931348623157e+308      # a very big number, let's call it LLL
1.7976931348623158e+308      # largest number according to Java's doc
1.7976931348623159e+308      # too large for float: becomes +inf
-1.7976931348623159e+308     # too negative-large: becomes -inf
-1.7976931348623157e+308 * 2  # is still -inf
17_976_931_348_623_157 * 10 ** 292          # LLL as integer
(17_976_931_348_623_157 * 10 ** 292) * 1.0  # LLL as integer as float
17_976_931_348_623_157 * 10 ** 293          # ten times LLL as integer
(17_976_931_348_623_157 * 10 ** 293) * 1.0  # causes OverflowError

from math import e, log
log(1.7976931348623157e+308)    # log(LLL) gives 709.782712893384
e ** 709.782712893384           # is smaller than LLL due to rounding
e ** 709.782712893385           # e^(log(LLL)+1e-12) -> OverflowError
1 / 1.7976931348623157e+308     # 5.562684646268003e-309
1 / 1.7976931348623159e+308     # == 1/inf == 0

from math import inf
inf == 1.7976931348623159e+308  # basically inf == inf, so it's True
inf == 1.7976931348623158e+308  # basically inf == LLL, so it's False
