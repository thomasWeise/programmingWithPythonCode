"""Example of the built-in functions exp, log and the constant e."""

from math import exp, log, e

print(exp(0) - 1)           # prints 0.0
print(exp(1) - e)           # prints 0.0
print(exp(2) - e ** 2)      # prints 8.881784197001252e-16
print(exp(3) - e ** 3)      # prints 3.552713678800501e-15
print(exp(4) - e ** 4)      # prints 7.105427357601002e-15

print(log(1))               # prints 0.0
print(log(e))               # prints 1.0
print(log(e ** 2))          # prints 2.0
print(log(e ** 3))          # prints 3.0
print(log(e ** 4))          # prints 4.0

print(log(exp(10))  - 10)   # prints 0.0
print(log(exp(0.1)) - 0.1)  # prints 6.938893903907228e-17
