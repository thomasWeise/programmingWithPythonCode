from math import inf
inf - 1      # infinity - 1 is still infinity
inf - 1e300  # infinity - big number is still infinity
inf - inf    # infinity - infinity is undefined == nan
inf / 1e300  # infinity / big number is still infinity
inf / inf    # infinity / infinity is still infinity
0 * inf      # 0 * infinity is undefined == nan

from math import nan
nan + 1      # undefined + anything = undefined
nan + inf    # undefined + anything = undefined
nan == 1     # undefined does not equal anything
nan != 1     # undefined is unequal to anything
1 != 1       # this is obviously False
nan == nan   # undefined does not equal anything, including itself
nan != nan   # undefined is unequal to anything, including itself
inf == inf   # infinity equals infinity
inf != inf   # infinity therefore does not "not equal" infinity
