"""
A class for rectangles.

>>> r = Rectangle(Point(22, 1), Point(4, 12))
>>> print(f"({r.p1.x},{r.p1.y}) - ({r.p2.x},{r.p2.y})")
(4,1) - (22,12)
"""

from typing import Final, Iterable

from point import Point
from polygon import Polygon


class Rectangle(Polygon):
    """A rectangle is defined by its bottom-left and top-right corners."""

    def __init__(self, p1: Point, p2: Point) -> None:
        """
        Create a rectangle.

        :param p1: the first point spanning the rectangle
        :param p2: the second point spanning the rectangle

        >>> try:
        ...     Rectangle(Point(1, 2), Point(3, 2))
        ... except ValueError as ve:
        ...     print(ve)
        p1.x=1, p1.y=2, p2.x=3, and p2.y=2 spans empty rectangle.
        """
        if (p1.x == p2.x) or (p1.y == p2.y):  # check for non-emptiness
            raise ValueError(f"p1.x={p1.x}, p1.y={p1.y}, p2.x={p2.x}, "
                             f"and p2.y={p2.y} spans empty rectangle.")
        #: the bottom-left point spanning the rectangle
        self.p1: Final[Point] = Point(min(p1.x, p2.x), min(p1.y, p2.y))
        #: the top-right point spanning the rectangle
        self.p2: Final[Point] = Point(max(p1.x, p2.x), max(p1.y, p2.y))

    def area(self) -> int | float:
        """
        Get the area of this rectangle.

        :return: the area of this rectangle

        >>> Rectangle(Point(7, 3), Point(12, 6)).area()
        15
        """
        return (self.p2.x - self.p1.x) * (self.p2.y - self.p1.y)

    def perimeter(self) -> int | float:
        """
        Get the perimeter of this rectangle.

        :return: the perimeter of this rectangle

        >>> Rectangle(Point(10, 5), Point(4, 9)).perimeter()
        20
        """
        return 2 * ((self.p2.x - self.p1.x) + (self.p2.y - self.p1.y))

    def points(self) -> Iterable[Point]:
        """
        Get the four corner points of this rectangle.

        :return: a generator yieling the four corners of this rectangle

        >>> list(f"{p.x},{p.y}" for p in Rectangle(
        ...     Point(1, 2), Point(3, 3)).points())
        ['1,2', '1,3', '3,3', '3,2']
        """
        yield self.p1  # the bottom-left point
        yield Point(self.p1.x, self.p2.y)  # the top-left point
        yield self.p2  # the top-right point
        yield Point(self.p2.x, self.p1.y)  # the bottom-right point
