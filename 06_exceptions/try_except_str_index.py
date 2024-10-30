"""Demonstrate `try...except` by looking for text in a string."""

text: str = "Hello World!"  # This is the string we search inside.

try:  # If this block raises an error, we continue at `except`.
    for s in ["Hello", "world"]:  # The strings we try to find.
        print(f"{s!r} is at index {text.index(s)}.")
except ValueError as ve:  # ValueError is raised if `s` isn't in `text`.
    print(ve)  # We get here because "world" is not in "Hello World!".

print("The program is now finished.")  # We get here after except block.
