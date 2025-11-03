""" For-Loop Example. """

for i in range(1, 10):
    s = ""
    for j in range(i):
        s += "*"
    print(f"{i}: {s}")
