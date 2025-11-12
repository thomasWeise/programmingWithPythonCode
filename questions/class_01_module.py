"""The person class."""

from typing import Final


class Person:
    """The person class."""

    def __init__(self, name: str, date_of_birth: str) -> None:
        #: the name
        self.name: Final[str] = name
        #: the date_of_birth
        self.date_of_birth: Final[str] = date_of_birth

    def introduce(self) -> None:
        """Introduce yourself."""
        print(f"Hello. My name is {self.name} and my "
              f"birthday is {self.date_of_birth}.")
