""" While-Loop Example. """

n: int = 20
vb: int = 1
r: float = 0.8
box: int = 100 ** 3
week: int = 1

print(f"start: {n} beetles, V/beetle: {vb}cm³,"
      f" reproduction_rate: {r}, V/box: {box}")

while True:
    n = int(n * (1 + r))
    v = vb * n
    print(f"week {week}: {n} beetles, V={v}cm³")
    if v >= box:
        break
    week += 1
