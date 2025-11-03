"""Lists: What output is produced by this program?"""

def fill_dictionary() -> dict[int, str]:
    """
    Fill a dictionary with some values.

    :return: the filled dictionary
    """
    a: dict[int, str] = {1: "one", 2: "two", 3: "three",
                         4: "four", 5: "five"}
    a.update({-k: f"minus {v}" for  k, v in a.items()})
    return a
