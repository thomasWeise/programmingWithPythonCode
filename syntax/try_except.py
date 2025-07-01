# The syntax of a try-except statement in Python.

try:  # Begin the try-except block.
    statement 1  # Code that may raise an exception or that
    statement 2  # calls a function that may rise one.
    # ...
except ExceptionType1 as ex1:  # One exception type that can be caught.
    statements processing ex1
    # Code the handles exceptions of type ExceptionType1.
except ExceptionType2 as ex2:  # Another exception type (optional).
    statements processing ex2
    # Code the handles exceptions of type ExceptionType2 that are not
    # instances of ExceptionType1.

next statement  # Executed only if there are no uncaught Exceptions.
