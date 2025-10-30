"""
Underhanded Python.

Find am argument value `X` for parameter `temperature` for which
`check_temperature` returns `True` even though `X` is not a floating
point number from the interval [0.0, 100.0].
"""

def check_temperature(temperature: int | float) -> bool:
    """
    Check whether a temperature setting for a water cooker is OK.

    :param temperature: the goal temperature that should be set
    :return: `True` if the temperature is permitted, `False` if not.
    """
    if (temperature < 0.0) or (temperature > 100.0):
        return False
    return True
