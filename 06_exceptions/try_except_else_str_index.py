"""Demonstrate `try...except...else` by looking for text in a string."""

text: str = "Hello World!"  # This is the string we search inside.

try:  # If this block raises an error, we continue at `except`.
    for s in ["Hello", "world"]:  # The strings we try to find.
        print(f"{s!r} is at index {text.index(s)}.")
except ValueError as ve:  # ValueError is raised if `s` isn't in `text`.
    print(ve)  # We get here because "world" is not in "Hello World!".
else:  # The else block is only invoked if no exception occurred.
    print("Everything is OK 1.")  # So we do not get here...

try:  # If this block raises an error, we continue at `except`.
    for s in ["Hello", "World"]:  # The strings we will be able to find.
        print(f"{s!r} is at index {text.index(s)}.")
except ValueError as ve:  # ValueError is raised if `s` isn't in `text`.
    print(ve)  # We never get here: This time, we look for "World".
else:  # The else block is only invoked if no exception occurred.
    print("Everything is OK 2.")  # So this time, this code is executed.
