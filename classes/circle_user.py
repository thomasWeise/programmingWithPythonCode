"""Examples for using our class :class:`Circle`."""

from circle import Circle  # Our new class `Circle`.
from point import Point    # Our very first class ever: `Point`.
from shape import Shape    # Our base class `Shape`.

circ: Circle = Circle(Point(2, 3), 5)  # Create a new circle instace.
print(f"                    center: ({circ.center.x}, {circ.center.y})")
print(f"                    radius: {circ.radius}")
print(f"                 perimeter: {circ.perimeter()}")
print(f"                      area: {circ.area()}")

# Do some instance tests.
print(f"  isinstance(circ, Circle): {isinstance(circ, Circle)}")
print(f"   isinstance(circ, Shape): {isinstance(circ, Shape)}")
print(f"  isinstance(circ, object): {isinstance(circ, object)}")

# Explore the class hierarchy.
print(f" issubclass(Circle, Shape): {issubclass(Circle, Shape)}")
print(f" issubclass(Shape, Circle): {issubclass(Shape, Circle)}")
print(f" issubclass(Shape, object): {issubclass(Shape, object)}")
print(f"issubclass(Circle, object): {issubclass(Circle, object)}")
