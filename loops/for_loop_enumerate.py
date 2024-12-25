"""Enumerate the index-value pairs in a list using enumerate."""

data: list[int] = [1, 2, 3, 5]
for i, v in enumerate(data):
    print(f"data[{i}]={v}")
