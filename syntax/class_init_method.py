"""The basic syntax for defining classes in Python."""

class MyClass:   # or `class MyClass(MyBaseClass)`
    """The docstring of the class."""

    def __init__(self) -> None:
        """The docstring of the initializer __init__."""
        # In this method, we initialize all the attributes of the class.
        # Each attribute should get an initial value, `None` if need be.

        #: Documentation of the meaning of attribute 1 (notice the ":"!)
        self.attribute_1: type hint = initial value
        # ...

    def my_method(self, param1: type hint, param2: type hint) -> result:
        """
        Docstring of my_method.

        :param param1: the documentation of the first parameter.
        :param param2: the documentation of the second parameter.
        :returns: the documentation of the result of the method.
        """
        # compute something using the attributes
