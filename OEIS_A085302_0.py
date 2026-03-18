import math

# Check if a number is prime
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# Compute primorial m#
def primorial(m):
    p = 1
    for i in range(2, m + 1):
        if is_prime(i):
            p *= i
    return p

# Cache primorials to speed up
primorial_cache = {}

def get_primorial(x):
    if x not in primorial_cache:
        primorial_cache[x] = primorial(x)
    return primorial_cache[x]

results = {}

n_max = 1000

for n in range(2, n_max+1):

    n_fact = math.factorial(n)
    n_prim = get_primorial(n)

    k = 1
    while True:
        k_prim = get_primorial(k)

        if n_fact < k_prim + n_prim:
            results[n] = k
            break

        k += 1


# Print original table
for n in results:
    print(f"n = {n}, first k = {results[n]}")


# -------- OEIS sequence extraction --------
prev_k = None
oeis_n = []
oeis_k = []

for n in sorted(results):
    k = results[n]
    if k != prev_k:
        oeis_n.append(n)
        oeis_k.append(k)
        prev_k = k


print("\nOEIS-style n sequence:")
print(",".join(map(str, oeis_n)))

print("\nCorresponding k values:")
print(",".join(map(str, oeis_k)))

print("\nPairs (n, k):")
for n, k in zip(oeis_n, oeis_k):
    print(f"({n}, {k})")
