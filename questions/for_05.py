""" Print a rectangle of Xes and Os."""

MAX: int = 7
for i in range(MAX):
    text: str = ""
    for j in range(MAX):
        text += "X" if ((i == j) or ((MAX - j - 1) == i)) else "O"
    print(text)
