1e-323  # = 1 * 10^-323
9e-324  # = 9 * 10^-324 -> gets rounded to 1 * 10^-323
8e-324  # = 8 * 10^-324 -> gets rounded to 1 * 10^-323
7e-324  # = 7 * 10^-324 -> gets rounded to 5 * 10^-324
6e-324  # = 6 * 10^-324 -> gets rounded to 5 * 10^-324
5e-324  # = 5 * 10^-324
4.94065645841246544e-324  # Smallest number in Java doc = 5 * 10^-324
4e-324  # = 4 * 10^-324 -> gets rounded to 5 * 10^-324
3e-324  # = 3 * 10^-324 -> gets rounded to 5 * 10^-324
2e-324  # = 2 * 10^-324: too small, becomes 0.0
1e-324  # = 1 * 10^-324: too small, becomes 0.0
0 == 3e-324  # basically: 0 == 5 * 10^-324 --> answer is False
0 == 2e-324  # basically: 0 == 0.0         --> answer is True
