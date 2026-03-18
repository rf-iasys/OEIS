# --- Prime helpers ---
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def generate_primes(n_max):
    primes = []
    candidate = 2
    while len(primes) < n_max:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

# --- Primorial helpers ---
primorial_cache = {0: 1}
def get_primorial(n, primes):
    if n in primorial_cache:
        return primorial_cache[n]
    max_cached = max(primorial_cache)
    p = primorial_cache[max_cached]
    for prime in primes:
        if max_cached < prime <= n:
            p *= prime
    primorial_cache[n] = p
    return p

# --- Inequality sequence ---
def inequality_sequence(n_max):
    primes = generate_primes(n_max + 50)
    factorial_cache = {0:1, 1:1}
    results = {}

    for n in range(2, n_max+1):
        n_fact = factorial_cache[n-1] * n
        factorial_cache[n] = n_fact
        n_prim = get_primorial(n, primes)

        k = 1
        while True:
            k_prim = get_primorial(k, primes)
            if n_fact < n_prim + k_prim:
                results[n] = k
                break
            k += 1

    # Extract OEIS-style jumps
    prev_k = None
    oeis_n = []
    oeis_k = []
    for n in sorted(results):
        k = results[n]
        if k != prev_k:
            oeis_n.append(n)
            oeis_k.append(k)
            prev_k = k
    return oeis_n, oeis_k

# --- OEIS A085302 and A085301 ---
def fn_oeis(x):
    """Largest k s.t. k! <= x"""
    k = 1
    r = x
    while r >= 1:
        k += 1
        r //= k
    return k - 1

def generate_A085302_and_parts(n_max):
    primes = generate_primes(n_max)
    primorials = [1]
    for p in primes:
        primorials.append(primorials[-1]*p)

    a085302 = []
    a085301_parts = []
    total = 0
    for i in range(1, n_max+1):
        if i <= 2:  # first two terms manually
            part = 2
        else:
            part = fn_oeis(primorials[i]) - fn_oeis(primorials[i-1])
        total += part
        a085302.append(total)
        a085301_parts.append(part)
    return a085302, a085301_parts

# --- Main ---
n_max = 10000  # adjust for full sequences

oeis_n, oeis_k = inequality_sequence(n_max)
a085302, a085301_parts = generate_A085302_and_parts(len(oeis_n))

# --- Display table ---
print(f"{'n':>4} {'k (ineq)':>10} {'OEIS A085302':>15} {'A085301 parts':>15}")
print("-"*60)
for i, n in enumerate(oeis_n):
    print(f"{n:4d} {oeis_k[i]:10d} {a085302[i]:15d} {a085301_parts[i]:15d}")

# --- Optional: first 20 terms of A085301 ---
print("\nFirst 20 OEIS A085301 terms (partial sums give A085302):")
print(a085301_parts[:20])
