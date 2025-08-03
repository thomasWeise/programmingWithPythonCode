"Hello World!"  # Both the double-quote and the single-quote can be
'Hello World!'  # used to define strings, but " is preferred.
"Hello" + ' ' + "World"  # Concatenate three strings.

len("Hello")  # Get the length of the string "Hello".

"Hello"[0]  # First character, "H"
"Hello"[1]  # Second character, "e"
"Hello"[2]  # Third character, "l"
"Hello"[3]  # Fourth character, "l"
"Hello"[4]  # Fifth character, "o"
"Hello"[5]  # Sixth character does not exist: Error!

"Hello"[-1]  # Last character: "o"
"Hello"[-2]  # Second-to-last character: "l"
"Hello"[-3]  # Third-to-last character: "l"
"Hello"[-4]  # Fourth-to-last character: "e"
"Hello"[-5]  # Fifth-to-last character: "H"
"Hello"[-6]  # Sixth-to-last character does not exist: Error!

"Hello"[0:3]  # Substring starting at index 0 and ending *before* 3.
"Hello"[1:3]  # Substring starting at index 1 and ending *before* 3.
"Hello"[2:]   # Substring starting at index 2, until end.
"Hello"[1:-2]  # Substring starting at index 1, ending before -2.
"Hello"[:-2]   # Everything before the second-to-last character.
"Hello World!"[1:8:2]  # Every 2nd character between indexes 1 and 8
