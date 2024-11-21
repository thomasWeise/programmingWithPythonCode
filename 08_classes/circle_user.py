"""Examples for using our class :class:`Circle`."""

from circle import Circle
from point import Point
from shape import Shape

circ: Circle = Circle(Point(2, 3), 5)
print(f"                  center: ({circ.center.x}, {circ.center.y})")
print(f"                  radius: {circ.radius}")
print(f"               perimeter: {circ.perimeter()}")
print(f"                    area: {circ.area()}")
print(f"isinstance(circ, Circle): {isinstance(circ, Circle)}")
print(f" isinstance(circ, Shape): {isinstance(circ, Shape)}")
