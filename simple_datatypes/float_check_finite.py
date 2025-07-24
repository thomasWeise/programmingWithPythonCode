from math import isfinite, isinf, isnan, nan, inf
isfinite(1e34)  # This is True, because 1 * 10^34 is big, but finite.
isfinite(inf)   # inf is not a finite number, so this is False.
isfinite(nan)   # And neither is nan, so we again get False.

isinf(0.3)   # 0.3 is not infinite. Not even close. So this is False.
isinf(-inf)  # -inf and inf are both infinite, so this is True.
isinf(nan)   # nan is undefined and not necessarily infinite: False.

isnan(0.3455)  # 0.3455 is a number, so it is not nan.
isnan(inf)     # inf is, technically, not a number, but also not nan.
isnan(nan)     # nan is certainly nan, so we get True.
