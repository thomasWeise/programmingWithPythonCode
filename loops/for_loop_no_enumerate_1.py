"""
Enumerate the index-value pairs in a list: Idea 1.

Lists and tuples can be indexed directly. Therefore, we can let the
index `i` go from `0` to `len(data)-1` and access the data elements by
using the index `i`. This would not work for stets or dicts.
"""

data: list[int] = [1, 2, 3, 5]  # The data to iterate over.

for i in range(len(data)):         # We iterate over indices and
    print(f"data[{i}]={data[i]}")  # use them to get the data elements.
