int_var = 1 + 7  # Create an integer variable holding an integer number.
print(type(int_var))  # This prints "<class 'int'>".

float_var = 3.0  # 3.0 is a float and it is stored in float_var.
print(type(float_var))  # This prints "<class 'float'>".

str_var = f"float_var={float_var}"  # Render an f-string into str_var.
print(type(str_var))  # This prints "<class 'str'>".

bool_var = (1 == 0)  # 1 == 0 is False, so a bool is stored in bool_var.
print(type(bool_var))  # This prints "<class 'bool'>".

none_var = None  # We create none_var which, well, holds None.
print(type(none_var))  # This prints "<class 'NoneType'>".
