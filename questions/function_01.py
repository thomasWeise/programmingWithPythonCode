""" An example of a function. """

def compute(lst: list[int]) -> list[int]:
    """
    Perform a computation with the list `lst`.

    :param lst: the input list
    :return: the output list
    """
    result: list[int] = []
    copy: list[int] = list(lst)

    while len(copy) > 0:
        x: int = min(copy)
        result.append(x)
        copy.remove(x)

    return result


print(compute([5, 4, 1, 3, 2]))      # Line 20: What does it print?
print(compute([25, -34, 6, -5, 9]))  # Line 21: What does it print?
