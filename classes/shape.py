"""
A base class for shapes defines a general interface for defining shapes.

It has no attributes, but two methods, `area` and `perimeter`, which
non-abstract subclasses must implement to return the area and perimeter
of the shapes they represent.

>>> from pytest import raises
>>> s = Shape()
>>> with raises(NotImplementedError):
...     s.area()
>>> with raises(NotImplementedError):
...     s.perimeter()
"""


class Shape:
    """A closed geometric shape has an area and a perimeter."""

    def area(self) -> int | float:
        """
        Get the area of this shape.

        :return: the area of this shape
        :raises NotImplementedError: You must overwrite this method.
        """
        raise NotImplementedError  # must be implemented by subclasses

    def perimeter(self) -> int | float:
        """
        Get the perimeter of this shape.

        :return: the perimeter of this shape
        :raises NotImplementedError: You must overwrite this method.
        """
        raise NotImplementedError  # must be implemented by subclasses
