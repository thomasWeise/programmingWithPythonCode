bin(22)       # Convert 22 to a text string with bit values.
0b10110       # 22 in binary notation, indicated by prefix 0b.
bin(15)       # Convert 15 to a text string with bit values.
0b1111        # 15 in binary notation, indicated by prefix 0b.

22 | 15       # bit-wise 'or' of 0b10110 and 0b1111
bin(31)       # Convert 31 to a text string with bit values.

22 & 15       # bit-wise 'and' of 0b10110 and 0b1111
bin(6)        # Convert 6 to a text string with bit values.

22 ^ 15       # bit-wise 'exclusive or' of 0b10110 and 0b1111
bin(25)       # Convert 25 to a text string with bit values.

22 << 1       # Shift 22 left by 1 step == 22 * 2.
bin(44)       # Convert 44 to a text string with bit values.

22 >> 2       # Shift 22 right by 2 steps == 22 // 4
bin(5)        # Convert 5 to a text string with bit values.

hex(22)       # Convert 22 to a string in hexadecimal notation.
0x16          # 22 in hexadecimal notation, indicated by prefix 0x.

oct(22)       # Convert 22 to a string in octal notation.
0o26          # 22 in octal notation, indicated by prefix 0o.
