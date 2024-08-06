# String and integer literals and identity.
a = "Hello World!"
b = "Hello World!"
print(f"Are 'a' and 'b' the same object: {a is b}")

c = "Hello " + "World!"
print(f"Are 'a' and 'c' the same object: {a is c}")

d = "Hello"
d = d + " World!"
print(f"Are 'a' and 'd' the same object: {a is d}")

e = 10
mul = 5
f = (e // mul) * mul
print(f"Are 'e' and 'f' the same object: {e is f}")

g = 1_000_000_000_000_000_000
h = (g // mul) * mul
print(f"Are 'g' and 'h' the same object: {g is h}")
