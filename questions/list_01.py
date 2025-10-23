"""Lists: What output is produced by this program?"""

a: list[int] = [1, 2, 3, 4]
a.append(5)
a.remove(3)
del a[2]
a.extend([5, 2])
a.sort()

print(a)
