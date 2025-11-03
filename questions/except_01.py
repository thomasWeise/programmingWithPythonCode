"""Safe factorial."""

def factorial(number: int) -> int:
    """
    Compute the factorial of a number. DO NOT CHANGE THIS FUNCTION.

    :param number: the number to compute the factorial of
    :return: `number!` for `number in 0...12`.
    :raises ValueError: if `number < 0` or `number > 12`.
    """
    if (number < 0) or (number > 12):
        raise ValueError(
            f"Cannot reasonably compute factorial of {number}.")
    for i in range(2, number):
        number *= i
    return number

# Modify this loop by using exception handling in order to prevent the
# program for crashing. Don't change the range of values `num` takes on!
for num in range(2, 20):
    print(f"{num}! = {factorial(num)}")
