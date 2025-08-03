"World" in "Hello World!"  # check if string is contained: yes
"Earth" in "Hello World!"  # check if string is contained: no

"Hello World!".find("World")  # get index of substring
"Hello World!".find("world")  # result -1 means "not found"
"Hello World!".find("l")      # search from start of string
"Hello World!".find("l", 3)   # search starting at index 3
"Hello World!".find("l", 4)   # search starting at index 4
"Hello World!".find("l", 10)  # starting at index 10: not found

"Hello World!".rfind("l")        # search backwards from end
"Hello World!".rfind("l", 2, 9)  # search backwards in range [2, 9)
"Hello World!".rfind("l", 0, 3)  # search backwards in range [0, 3)
"Hello World!".rfind("l", 0, 2)  # search backwards in range [0, 2)

"Hello World!".replace("Hello", "Hi")             # replace all
"Hello World! Hello!".replace("Hello", "Hi")      # occurrences, but
"Hello World!".replace("Hello", "Hello! Hello!")  # not recursively

" Hello World! ".strip()   # Remove leading and trailing spaces.
" Hello World! ".lstrip()  # Remove leading spaces.
" Hello World! ".rstrip()  # Remove trailing spaces.

"Hello World!".lower()  # Convert to lower case.
"Hello World!".upper()  # Convert to upper case.

"Hello World!".startswith("hello")  # Checking if string starts with
"Hello World!".startswith("Hello")  # text is case-sensitive.

"Hello World!".endswith("Hello")   # Checking if string ends with
"Hello World!".endswith("World!")  # text is case-sensitive, too.
