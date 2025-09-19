"""The basic syntax for defining classes in Python."""

class MyClass:   # or `class MyClass(MyBaseClass)`
    """The docstring of the class."""

    def __init__(self, param1: type_hint) -> None:
        """The docstring of the initializer __init__."""
        # In this method, we initialize all the attributes of the class.
        # Each attribute should get an initial value, `None` if need be.

        #: Documentation of the meaning of attribute 1 (notice the ":"!)
        self.attribute_1: type_hint = initial value
        # ...

    def my_method(self, param1: type_hint, param2: type_hint) -> result:
        """
        Docstring of my_method.

        :param param1: the documentation of the first parameter.
        :param param2: the documentation of the second parameter.
        :returns: the documentation of the result of the method.
        """
        # compute something using the attributes
        self.attribute_1 = ...    # Assign value to attribute.
        x = self.attribute_1      # Use the value of an attribute.
        self.my_other_method(12)  # Call other methods of the class.

    # ... more methods


# Instantiating MyClass creates a new instance of MyClass.
# We can use MyClass as type hint for variables.
newVar: MyClass = MyClass(value for param1 of __init__)
