"""Examples of `map`."""

csv_data: str = "12,23,445,3,12,6,-3,5"

csv_data_as_ints: list[int] = list(map(int, csv_data.split(",")))
print(f"csv_data_as_ints: {csv_data_as_ints}")

csv_data_sqrs: set[int] = set(map(lambda x: x ** 2, csv_data_as_ints))
print(f"csv_data_sqrs: {csv_data_sqrs}")

words: list[str] = ["Hello", "world", "How", "are", "you"]
print(f"longest word length: {max(map(len, words))}")
