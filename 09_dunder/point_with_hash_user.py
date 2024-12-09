"""Examples for using our class :class:`Point` with hash."""

from point_with_hash import Point

p1: Point = Point(3, 5)  # Create a first point.
p2: Point = Point(7, 8)  # Create a second, different point.
p3: Point = Point(3, 5.0)  # A third point, which equals the first.

print(f"{(p1 == p2) = }")  # False, since p1 is really != p2
print(f"{(p1 == p3) = }")  # True, since p1 equals p3

points: set[Point] = {p1, p2, p3}  # This set will contain 2 points.
print(f"{points = }")  # The set of two points, because p1 == p2.
print(f"{p1 in points = }")  # True
print(f"{p2 in points = }")  # True
print(f"{p3 in points = }")  # True
print(f"{Point(7.0, 8.0) in points = }")  # True: point is equal to p2
print(f"{Point(3.1, 5) in points = }")  # False: point is not in the set

# A dictionary with points as keys.
point_vals: dict[Point, str] = {p1: "A", p2: "B"}
print(f"{point_vals = }")  #  {Point(3, 5): 'A', Point(7, 8): 'B'
point_vals[Point(7, 9)] = "C"  # Put a new point/string-item in the dict
print(f"{point_vals = }")  # Now there are three items.
