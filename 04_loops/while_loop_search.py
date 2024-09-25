"""Using a `while` loop to implement Binary Search."""

data: str = "abdfjlmoqsuvwyz"  # A string of sorted characters.

for search in ["a", "c", "o", "p", "w", "z"]:  # Search 6 characters.
    upper: int = len(data)  # *Exclusive* upper index.
    lower: int = 0  # Lowest possible index = 0 (inclusive).
    while lower < upper:  # Repeat until lower >= upper.
        mid: int = (lower + upper) // 2  # Works ONLY in Python :-).
        mid_str = data[mid]  # Get the character at index mid.
        if mid_str < search:  # If mid_str < search, then clearly...
            lower = mid + 1  # ...the index of search must be < mid.
        elif mid_str > search:  # If mid_str > search, then clearly...
            upper = mid  # ...the index of search must be > mid.
        else:  # If neither (mid_str < search) nor (mid_str > search)...
            print(f"Found {search!r} at index {mid} in {data!r}.")
            break  # Exit while loop and skip over while loop's else.
    else:  # executed if the while condition is False; not after break
        print(f"Did not find {search!r} in {data!r}.")
