""" An example of a function. """

def compute(number: int) -> int:
    """
    Perform a computation with the number `number`.

    :param number: the input number
    :return: the output num
    """
    result: int = 0
    while result / number != number:
        result += number

    return result


print(compute(4))  # Line 16: What does it print?
print(compute(7))  # Line 17: What does it print?
print(compute(0))  # Line 18: What does it print?
