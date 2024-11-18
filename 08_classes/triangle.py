"""
A class for triangles.

>>> t = Triangle(Point(22, 1), Point(4, 12), Point(6, 3))
>>> print(f"{t.p1.x},{t.p1.y} - {t.p2.x},{t.p2.y} - {t.p3.x},{t.p3.y}")
22,1 - 4,12 - 6,3

>>> Triangle(Point(0, 0), Point(0, 3), Point(4, 0)).perimeter()
12.0
"""

from typing import Final, Iterable

from point import Point
from polygon import Polygon


class Triangle(Polygon):
    """The class for triangles."""

    def __init__(self, p1: Point, p2: Point, p3: Point) -> None:
        """
        Create a triangle.

        :param p1: the first point spanning the triangle
        :param p2: the second point spanning the triangle
        :param p3: the third point spanning the triangle

        >>> try:
        ...     Triangle(Point(1, 2), Point(3, 2), Point(1, 2))
        ... except ValueError as ve:
        ...     print(ve)
        p1=1,2, p2=3,2, p3=3,2 span an empty triangle.
        """
        if (p1.distance(p2) <= 0) or (p2.distance(p3) <= 0) or (
                p3.distance(p1) <= 0):  # check for non-emptiness
            raise ValueError(f"p1={p1.x},{p1.y}, p2={p2.x},{p2.y}, p3="
                             f"{p2.x},{p3.y} span an empty triangle.")
        #: the first point spanning the triangle
        self.p1: Final[Point] = p1
        #: the second point spanning the triangle
        self.p2: Final[Point] = p2
        #: the trird point spanning the triangle
        self.p3: Final[Point] = p3

    def area(self) -> int | float:
        """
        Get the area of this triangle.

        :return: the area of this triangle

        >>> Triangle(Point(0, 0), Point(0, 1), Point(2, 0)).area()
        1.0
        >>> Triangle(Point(-1, 2), Point(2, 3), Point(4, -3)).area()
        10.0
        """
        return 0.5 * abs(self.p1.x * (self.p2.y - self.p3.y)
                         + self.p2.x * (self.p3.y - self.p1.y)
                         + self.p3.x * (self.p1.y - self.p2.y))

    def points(self) -> Iterable[Point]:
        """
        Get the three points describing this triangle.

        :return: a generator yielding the three corners of this triangle

        >>> list(f"{p.x},{p.y}" for p in Triangle(
        ...     Point(1, 2), Point(3, 3), Point(4, 5)).points())
        ['1,2', '3,3', '4,5']
        """
        yield self.p1  # Return the first point in the iteration.
        yield self.p2  # Return the second point in the iteration.
        yield self.p3  # Return the third point in the iteration.
