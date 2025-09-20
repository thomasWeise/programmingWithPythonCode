"""Example of using our class where we change the `Final` attributes."""

from point import Point         # Import our class from its module.

p1: Point = Point(3, 5)         # Create a first instance of Point.
print(f"{p1.x = }, {p1.y = }")  # p1.x = 3, p1.y = 5

p1.x = 5                        # This is not allowed, but possible!
print(f"{p1.x = }, {p1.y = }")  # p1.x = 5, p1.y = 5
