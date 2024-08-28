"""An example for using the `if-else` statement."""

year: int = 2024  # the year 2024 should be a leap year
if (((year % 4) == 0) and ((year % 100) != 0)) or ((year % 400) == 0):
    print(f"{year} is a leap year.")
    print("yes, it really is.")
else:
    print(f"{year} is not a leap year.")

year = 1900  # the year 1900 is not a leap year
if (((year % 4) == 0) and ((year % 100) != 0)) or ((year % 400) == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    print("Believe you me, it indeed is not.")
