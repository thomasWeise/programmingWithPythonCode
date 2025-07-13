from math import isfinite, isinf, isnan, nan, inf
isfinite(1e34)
isfinite(inf)
isfinite(nan)

isinf(0.3)
isinf(-inf)

isnan(0.3455)
isnan(inf)
isnan(nan)
