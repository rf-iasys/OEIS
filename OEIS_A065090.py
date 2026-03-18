import math

# --- Parameter m for n! <= n# * m^k ---
m = math.e

# --- Prime helpers ---
def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: return False
    return True

def generate_primes(n_max):
    primes = []
    candidate = 2
    while len(primes) < n_max:
        if is_prime(candidate): primes.append(candidate)
        candidate += 1
    return primes

# --- Primorial ---
primorial_cache = {0:1}
def get_primorial(n, primes):
    if n in primorial_cache: return primorial_cache[n]
    max_cached = max(primorial_cache)
    p = primorial_cache[max_cached]
    for prime in primes:
        if max_cached < prime <= n: p *= prime
    primorial_cache[n] = p
    return p

# --- Factorial ---
factorial_cache = {0:1, 1:1}
def factorial(n):
    if n in factorial_cache:
        return factorial_cache[n]
    factorial_cache[n] = factorial(n-1) * n
    return factorial_cache[n]

# --- Inequality sequence n! <= n# * m^k ---
def inequality_sequence_n_pow_k(n_max, m):
    primes = generate_primes(n_max + 50)
    results = {}
    for n in range(2, n_max+1):
        n_fact = factorial(n)
        n_prim = get_primorial(n, primes)
        k = 0
        while True:
            if n_fact <= n_prim * m**k:
                results[n] = k
                break
            k += 1
    return results

# --- Example usage ---
n_max = 100
results = inequality_sequence_n_pow_k(n_max, m)

# --- Print n vs k table ---
print(f"{'n':>4} {'k (ineq n! <= n# * m^k)':>30}")
print("-"*40)
for n in sorted(results):
    print(f"{n:4d} {results[n]:30d}")

# --- Compute first n per k (OEIS-style sequences) ---
first_n_dict = {}
for n, k in results.items():
    if k not in first_n_dict:
        first_n_dict[k] = n

# Sort by k to produce sequences
first_n_oeis = [first_n_dict[k] for k in sorted(first_n_dict)]
k_oeis = [k for k in sorted(first_n_dict)]

# --- Print first n per k ---
print("\nFirst n per k (OEIS-style sequences) for n! <= n# * m^k")
print(f"\n{'first n':>8} {'k':>3}")
print("-"*20)
for n_val, k_val in zip(first_n_oeis, k_oeis):
    print(f"{n_val:8d} {k_val:3d}")

# --- Optional: sequences separately ---
print("\nOEIS-style sequence of first n per k:", first_n_oeis)
print("\nOEIS-style sequence of corresponding k values:", k_oeis)
