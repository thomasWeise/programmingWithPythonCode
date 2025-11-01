"""
Underhanded Python.

Create an argument for the `to_str` function that causes it to crash.
"""

class Entry:
    """A class for a linked list."""

    def __init__(self, value: str, next: "Entry | None" = None) -> None:
        """
        Create the list entry.
        :param value: the value string of the list element
        :param next: the next element in the list
        """
        self.value: str = value
        self.next: "Entry | None" = next


def to_str(head: Entry | None) -> str:
    """
    Concatenate all value strings in the linked list `head`.

    :param head: the head of the list
    :return: the concatenation of all values in the linked list.

    >>> to_str(None)
    ''
    >>> to_str(Entry("x"))
    'x'
    >>> to_str(Entry("x", Entry("y")))
    'xy'
    >>> to_str(Entry("x", Entry("y", Entry("z"))))
    'xyz'
    """
    result: str = ""  # Set the initial result to the empty strong.

    while head is not None:   # Iterate until the end of the list.
        result += head.value  # Append the current value to the result.
        head = head.next      # Move to the next element.

    return result  # Return the result string.
