# Python's float supports 15 to 16 digits of precision.

1e15 + 1         # This works and will give us 1_000_000_000_000_001.
1e16 + 1         # This gives us 1e16, because we would need 17 digits.
1e16 + 1 - 1e16  # Since 1e16 + 1 == 1e16, this does yield 0.

1e18 + 1e36      # 1_000_000_000_000_000_001 * 1e18 needs 19 digits...
1e18 + 1e36 - 1e36  # Since 1e18 + 1e36 == 1e36, this will give us 0.
1e18 + 1 + 1e36 - 1e36 - 1e18  # The correct result would be 1... but...
