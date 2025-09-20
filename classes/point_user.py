"""Examples of using our class :class:`Point`."""

from point import Point            # Import our class from its module.

p1: Point = Point(3, 5)            # Create a first instance of Point.
print(f"{p1.x = }, {p1.y = }")     # p1.x = 3, p1.y = 5

print(f"{type(p1) = }")               # <class 'point.Point'>
print(f"{isinstance(p1, Point) = }")  # Hence, this is True.
print(f"{isinstance(5, Point) = }")   # This is obviously False.
print(f"{isinstance(p1, int) = }")    # This is obviously False, too.

p2: Point = Point(x=7, y=8)        # Create a second instance of Point.
print(f"{p2.x = }, {p2.y = }")     # p2.x = 7, p2.y = 8
print(f"{type(p2) = }")            # <class 'point.Point'>

print(f"{p1 is p1 = }")  # True, because p1 is the same as p1.
print(f"{p1 is p2 = }")  # False, as these are two different instances.

print(f"{p1.distance(p2) = }")  # sqrt(4² + 3²) = 5.0
print(f"{p2.distance(p1) = }")  # sqrt(4² + 3²) = 5.0

point_list: list[Point] = [  # Create list of points via comprehension.
    Point(x, y) for x in range(3) for y in range(2)]
print(", ".join(f"({p.x}, {p.y})" for p in point_list))
