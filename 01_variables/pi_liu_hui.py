from math import pi, sqrt

print(f"We use Liu Hui's Method to Approximate \u03c0={pi}.")
e = 6  # the number of edges: We start with a hexagon, i.e., e=6.
s = 1  # the side length: Initially 1, meaning the radius is also 1.
print(f"{e} edges, side length={s} give us \u03c0={e * s / 2}.")

e *= 2  # We double the number of edges...
s = sqrt(2 - sqrt(4 - (s ** 2)))  # ...and recompute the side length.
print(f"{e} edges, side length={s} give us \u03c0={e * s / 2}.")

e *= 2  # We double the number of edges.
s = sqrt(2 - sqrt(4 - (s ** 2)))  # ...and recompute the side length.
print(f"{e} edges, side length={s} give us \u03c0={e * s / 2}.")

e *= 2  # We double the number of edges.
s = sqrt(2 - sqrt(4 - (s ** 2)))  # ...and recompute the side length.
print(f"{e} edges, side length={s} give us \u03c0={e * s / 2}.")

e *= 2  # We double the number of edges.
s = sqrt(2 - sqrt(4 - (s ** 2)))  # ...and recompute the side length.
print(f"{e} edges, side length={s} give us \u03c0={e * s / 2}.")

e *= 2  # We double the number of edges.
s = sqrt(2 - sqrt(4 - (s ** 2)))
print(f"{e} edges, side length={s} give us \u03c0={e * s / 2}.")
