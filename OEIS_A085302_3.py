# --- Prime helpers ---
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# Generate first n primes
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
    """Compute n# incrementally using primes list and cache."""
    if n in primorial_cache:
        return primorial_cache[n]
    # Find the largest cached primorial <= n
    max_cached = max(primorial_cache)
    p = primorial_cache[max_cached]
    for prime in primes:
        if max_cached < prime <= n:
            p *= prime
    primorial_cache[n] = p
    return p

# --- Integer-only inequality sequence ---
def inequality_sequence(n_max):
    """
    Compute smallest k for each n such that:
        n! < n# + k#
    Returns OEIS-style jumps (n, k)
    """
    # Precompute first n_max primes
    primes = generate_primes(n_max + 50)  # extra for k > n
    factorial_cache = {0: 1, 1: 1}
    results = {}

    for n in range(2, n_max + 1):
        # Incremental factorial
        n_fact = factorial_cache[n-1] * n
        factorial_cache[n] = n_fact

        # Incremental primorial for n
        n_prim = get_primorial(n, primes)

        # Find smallest k with n! < n# + k#
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

# --- OEIS A085302 generator ---
def fn_oeis(x):
    """Compute the OEIS function in integer arithmetic."""
    k = 1
    r = x
    while r >= 1:
        k += 1
        r //= k  # integer division avoids overflow
    return k - 1

def generate_A085302(n_max):
    """Generate A085302 using incremental primorials."""
    primes = generate_primes(n_max)
    sequence = []
    n_prim = 1  # incremental primorial

    for i, p in enumerate(primes, start=1):
        n_prim *= p
        if i == 1:
            sequence.append(2)
        else:
            sequence.append(fn_oeis(n_prim) + 1)
    return sequence

# --- Main ---
n_max = 1000

oeis_n, oeis_k = inequality_sequence(n_max)
a085302 = generate_A085302(len(oeis_n))

print("OEIS-style n sequence:", oeis_n)
print("\nCorresponding k values:", oeis_k)
print("\nOEIS A085302 locally:", a085302)

# Direct comparison
match = all(a == b for a, b in zip(oeis_n, a085302))
print("\n✅ Direct match:", match)
