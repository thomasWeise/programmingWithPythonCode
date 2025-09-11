"""The syntax of the `raises` context manager offered by `pytest`."""

from pytest import raises  # Needed checking that exceptions are raised.

# `raises` is a context manager that will cause the test to fail if no
# exception of type `ExceptionType` is raised.
with raises(ExceptionType):
    code that should raise ExceptionType

# We can provide a regular expression with parameter `match`.
# If either no exception of type `ExceptionType` is raised
#                   >>> OR <<<<
# If the error message stored in the exception does not match to this
# regex, then the test will fail.
with raises(ExceptionType, match="error message regex"):
    code that should raise ExceptionType  with error message
