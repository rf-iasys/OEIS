from sympy import primerange
from math import factorial
from collections import defaultdict

# Compute primorial
def primorial(n):
    product = 1
    for p in primerange(1, n+1):
        product *= p
    return product

N = 400
k_per_n = []

# Find smallest k such that n! < n# + k#
for n in range(1, N+1):
    nf = factorial(n)
    nph = primorial(n)
    
    k = 1
    while nph + primorial(k) <= nf:
        k += 1
    
    k_per_n.append((n, k))

# Collect second n for each k
k_to_ns = defaultdict(list)
for n, k in k_per_n:
    k_to_ns[k].append(n)

second_n_list = [ns[1] for ns in k_to_ns.values() if len(ns) > 1]

# Sort and print OEIS-style
second_n_list.sort()
print("OEIS-style sequence:", ", ".join(map(str, second_n_list)))
