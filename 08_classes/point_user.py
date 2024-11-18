"""Examples for using out class :class:`Point`."""

from point import Point

p1: Point = Point(3, 5)  # Create a first point.
print(f"p1.x = {p1.x}, p1.y = {p1.y}")  # p1.x = 3, p1.y = 5
print(f"isinstance(p1, Point): {isinstance(p1, Point)}")  # True

p2: Point = Point(7, 8)  # Create a second point.
print(f"p2.x = {p2.x}, p2.y = {p2.y}")  # p2.x = 7, p2.y = 8
print(f"isinstance(p2, Point): {isinstance(p2, Point)}")  # True

print(f"isinstance(5, Point): {isinstance(5, Point)}")  # False

print(f"p1 is p2: {p1 is p2}")  # False

print(f"p1.distance(p2): {p1.distance(p2)}")  # sqrt(4² + 3²) = 5.0
print(f"p2.distance(p1): {p2.distance(p1)}")  # sqrt(4² + 3²) = 5.0

point_list: list[Point] = [  # Create list of points via comprehension.
    Point(x, y) for x in range(3) for y in range(4)]
print(", ".join(f"({p.x}, {p.y})" for p in point_list))
