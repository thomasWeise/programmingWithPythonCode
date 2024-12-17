# start part_1
"""An API for XML output via context managers and `with`."""

from typing import Any, Callable, Final, Literal, Self

#: An internal mapping for escaping reserved XML characters.
_ESC: Final = str.maketrans({"<": "&#38;", ">": "&#62;", "'": "&#39;"})


class Element:
    """An XML element. XML elements can be nested arbitrarily deeply."""

    def __init__(self, dest: Callable[[str], Any],
                 name: str, attrs: dict[str, Any] | None = None,
                 is_root: bool = True) -> None:
        """
        Create the XML element.

        :param dest: the function to receive the text output
        :param name: the name of the element
        :param attrs: the attributes, if any, otherwise `None`
        :param is_root: is this the root element?
        """
        #: the destination, i.e., a function receiving all the output
        self.__dest: Final[Callable[[str], Any]] = dest  # protected var

        head: list[str] = ['<?xml version="1.0"?>\n'] if is_root else []
        head.append(f"<{name}")
        if attrs:  # If attrs is neither None nor empty...
            for key, value in attrs.items():  # ...append as key='value'
                head.append(f" {key}={str(value).translate(_ESC)!r}")
        head.append(">")  # Close the element start.

        #: the header: XML declaration (if root) plus the element start
        self.__head: Final[str] = "".join(head)  # Merge string list.
        #: the element closing text, i.e., something like `</myElement>`
        self.__foot: Final[str] = f"</{name}>"

    def __enter__(self) -> Self:
        """
        Enter the XML element context and write the element start text.

        :returns: this element itself
        """
        self.__dest(self.__head)  # write the header
        return self  # Return this object itself.

    def __exit__(self, *exc) -> Literal[False]:
        """
        We are done with this context: Close the XML element.

        :param exc: the exception information, which we ignore
        :returns: always `False`
        """
        self.__dest(self.__foot)  # write the element closing
        return False  # re-raise exception that occurred in with, if any
# end part_1

# start part_2
    def element(self, name: str,
                attrs: dict[str, Any] | None = None) -> "Element":
        """
        Create a new XML Element inside this element.

        :param name: the name of the element
        :param attrs: the attributes, if any, otherwise `None`
        :return: the new element
        """
        return Element(self.__dest, name, attrs, False)

    def text(self, txt: str) -> None:
        """
        Write some textual content inside this XML element.

        :param txt: the text to be written.
        """
        self.__dest(txt.translate(_ESC))  # Write the text.
# end part_2
