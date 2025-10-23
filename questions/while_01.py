""" While-Loop Example. """

a, b, c, d, e = 5, 3, 2, 1, 0
counter = 0

while not (a < b < c < d < e):
    counter += 1
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if c > d:
        c, d = d, c
    if d > e:
        d, e = e, d

print(f"Loop finished after {counter} iterations.")
