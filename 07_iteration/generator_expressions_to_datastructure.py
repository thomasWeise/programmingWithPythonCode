"""Using generator expressions to create collections."""

csv_text: str = "22,56,33,67,43,12"

as_list: list[int] = list(int(i) for i in csv_text.split(","))
print(f"a generator converted to list: {as_list}.")

as_sorted_list: list[int] = sorted(int(i) for i in csv_text.split(","))
print(f"a generator converted to sorted list: {as_sorted_list}.")

as_dict: dict[str, int] = dict((i, int(i)) for i in csv_text.split(","))
print(f"a generator of tuples converted to dict: {as_dict}.")
