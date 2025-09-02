"""
Enumerate the index-value pairs in a list using enumerate.

We now use the function `enumerate` to generate a sequence of
index-value pairs and directly unpack them in the loop header into the
variables `i` (for the index) and `v` (for the value).
"""

data: list[int] = [1, 2, 3, 5]  # The data to iterate over.

for i, v in enumerate(data):  # Generate index-value pair sequence...
    print(f"data[{i}]={v}")
