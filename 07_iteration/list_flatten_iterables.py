"""A utility for flatten sequences of sequences."""

from typing import Iterable


def flatten(iterables: Iterable[Iterable]) -> list:
    """
    Flatten an :class:`Iterable` of `Iterable`s.

    :param iterables: the `Iterable` containing other `Iterable`s.
    :return: a single list with all the contents

    >>> flatten([[1, 2, 3], [4, 5, 6]])
    [1, 2, 3, 4, 5, 6]

    >>> flatten(([1, 2, 3], (4, 5, 6), {"a": 7, "b": 8}))
    [1, 2, 3, 4, 5, 6, 'a', 'b']

    >>> flatten(([1, 2, 3], [[4], [5], [6, 7]]))
    [1, 2, 3, [4], [5], [6, 7]]

    >>> flatten(flatten([[[1], [2, 3]], [[4, 5], [6]]]))
    [1, 2, 3, 4, 5, 6]
    """
    return [value for subiterable in iterables for value in subiterable]
