"""Examples for using the different :class:`Shape` classes."""

from circle import Circle        # Our new class `Circle`.
from point import Point          # Our very first class ever: `Point`.
from rectangle import Rectangle  # Our new class `Rectangle`.
from triangle import Triangle    # Our new class `Triangle`.
from shape import Shape          # Our base class `Shape`.
from typing import Final         # Type hint for immutable variables.

shapes: Final[list[Shape]] = [   # We create list of shapes.
    Circle(Point(2, 3), 5),
    Rectangle(Point(2, 3), Point(3, 5)),
    Triangle(Point(2, 3), Point(3, 5), Point(7, 4)),
]

for s in shapes:  # Print shape classes, areas, and perimeters.
    print(f"{type(s)} instance with A={s.area()} and P={s.perimeter()}")
