"""
Enumerate the index-value pairs in a list: Idea 2.

We can iterate over any container class directly with a for loop.
In this case, we simply increment the index by ourselves.
"""

data: list[int] = [1, 2, 3, 5]  # The data to iterate over.

i = 0           # The initial index is 0.
for v in data:  # We iterate over the data values directly.
    print(f"data[{i}]={v}")
    i += 1      # And we increment the index by ourselves.
