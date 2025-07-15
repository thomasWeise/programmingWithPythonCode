f"{12345678901234} is a really big integer."
f"12345678901234 with thousand separator ',' is {12345678901234:,}."
f"{12345678901234} in hexadecimal notation is {12345678901234:x}."
f"{12345678901234} in 0x-hexadecimal notation is {12345678901234:#x}."
f"{1234567890} in binary notation is {1234567890:b}."
f"{1234567890} in 0b-binary notation is {1234567890:#b}."

f"{5} + {4} = {5 + 4}"

from math import pi
f"pi is approximately {pi}."
f"pi rounded to two decimals is {pi:.2f}."

f"1/321 as percentage with 2 decimals is {1/321:.2%}."
f"1.2345533e6 with thousand separator and 1 decimal is {1.2345533e6:,.1f}."

from math import sin
f"sin(0.25pi) is approximately {sin(0.25*pi):.5f}."
f"{1.2359817e12} is {1.2359817e12:e} and approximately {1.2359817e12:.3g}."

f"Single braces without expression: {{ and }}."

f"{5 + 4 = }"
f"{23 * sin(2 - 5) = }"
