"""Run a simulated REPL mode."""

from code import InteractiveConsole
from sys import argv, platform, version
from typing import Final

# The constants for new and continued statement prefixes.
NEW_STATEMENT: Final[str] = ">>> "
CONTINUED_STATEMENT: Final[str] = "... "

# Printing the python header
print(f"Python {version} on {platform}")
print('Type "help", "copyright", "credits" or "license" for more information.')


def run(code: list[str], console = InteractiveConsole()) -> None:
    """
    Run a piece of code.

    :param code: the code to run.
    :param console: the console (dodgy use of defaults)
    """
    if not code:
        return  # exit if code is empty
    if console.push("\n".join(code)):
        console.push("")  # force multi-line statements to close
    code.clear()  # Clear code.


# first we read all the code
with open(argv[1]) as file:
    lines: list[str] = list(map(str.strip, file.readlines()))

cur: list[str] = []  # the current list of statements

for line in lines:  # we go over the lines to collect statements
    if line.startswith(CONTINUED_STATEMENT):
        print(line)  # continued statements are collected
        cur.append(line[str.__len__(CONTINUED_STATEMENT):])
    elif line.startswith(NEW_STATEMENT):
        if list.__len__(cur) > 0:
            run(cur)  # execute all collected statements
        print(line)  # print code line
        cur.append(line[str.__len__(NEW_STATEMENT):])
    elif str.__len__(line) > 0:  # wrong prefix, raise error.
        if list.__len__(cur) > 0:
            run(cur)  # execute all collected statements
        print(f"{NEW_STATEMENT}{line}")  # print code line
        cur.append(line)
    else:  # no code: ends last block of code
        run(cur)
        print()  # print an empty line

run(cur)  # Execute left-over statements
