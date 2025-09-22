# Python's float supports 15 to 16 digits of precision.

1e15 + 1         # This works and will give us 1_000_000_000_000_001
1e16 + 1         # This gives us 1e16, since we would need 17 digits

# While 1e16 + 1 cannot be represented exactly with a `float`, one
# may wonder what happens if the computation produces results that
# can be represented exactly ... but has intermediate steps that
# would exceed the range that can be covered by a `float`.
1e16 + 1 - 1e16  # Since 1e16 + 1 == 1e16, this does yield 0.

# The problems with the range of `float` can also occur if we have
# two very large numbers ... as long as one is much larger than the
# other.
1e18 + 1e36      # 1_000_000_000_000_000_001 * 1e18 needs 19 digits

# We here can again observe the problem with intermediate results.
# The final result may fit well into a `float`, but if precision is
# lost in intermediate steps, the final result can be off quite a
# bit.
1e18 + 1e36 - 1e36  # Since 1e18 + 1e36 == 1e36, this gives us 0.
1e18 + 1 + 1e36 - 1e36 - 1e18  # The exact result would be 1, but...
