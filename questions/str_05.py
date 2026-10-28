"""Using the Result of 'find' as Index."""

text: str = "Hello World!"  # Store "Hello World!" in variable 'text'.

print(text.find("World"))         # Line 5

print(text[text.find("World")])   # Line 7
print(text[text.find("World"):])  # Line 8

print(text[text.find("world")])   # Line 10
print(text[text.find("world"):])  # Line 11
