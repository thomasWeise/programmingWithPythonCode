"""An example for creating and using sets."""

odd: set[int] = {1, 3, 5, 7, 9, 11, 13, 15}  # a subset of odd numbers
print(f"some odd numbers are: {odd}")  # print the set
prime: set[int] = {2, 3, 5, 7, 11, 13}  # a subset of the prime numbers
print(f"some prime numbers are: {prime}")  # print the set

set_or: set[int] = odd.union(prime)  # create a new set as union of both
print(f"{len(set_or)} numbers are in odd \u222A prime: {set_or},")

set_and: set[int] = odd.intersection(prime)  # compute the intersection
print(f"{len(set_and)} are in odd \u2229 prime: {set_and},")

# get the numbers that are in one and only one of the two sets
set_xor: set[int] = odd.symmetric_difference(prime)
print(f"{len(set_xor)} are in (odd \u222A prime) "
      f"\u2216 (odd \u2229 prime): {set_xor},")

only_odd: set[int] = odd.difference(prime)  # odd but not prime
print(f"{len(only_odd)} are in odd \u2216 prime: {only_odd}, and")

only_prime: set[int] = prime.difference(odd)  # prime but not odd
print(f"{len(only_prime)} are in prime \u2216 odd: {only_prime}")
