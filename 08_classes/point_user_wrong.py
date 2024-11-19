"""Examples for using out class :class:`Point` **incorrectly**."""

from point import Point

p: Point = Point(3, 5)  # Create a first point.
p.z = 23  # Add another attribute outside `__init__`.
print(f"p.x = {p.x}, p.y = {p.y}, p.z = {p.z}")

p.x = 12  # Change a attribute marked as `Final`.
print(f"p.x = {p.x}, p.y = {p.y}, p.z = {p.z}")


class OtherClass:
    """A totally different class that also has attributes x and y."""

    def __init__(self, x: int, y: int) -> None:
        """
        Create an instance of OtherClass.

        :param x: the value for attribute `x`
        :param y:  the value for attribute `y`
        """
        self.x: int = x
        self.y: int = y


print(f"distance used incorrectly: {p.distance(OtherClass(1, 2))}",
      flush=True)

print(f"distance used incorrectly again: {p.distance(2)}")
