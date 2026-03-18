import math

# Generate first n primes
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

# Compute n-th primorial
def primorial(n, primes):
    p = 1
    for i in range(n):
        p *= primes[i]
    return p

# OEIS fn[n] function
def fn(n):
    k = 1
    r = n
    while r >= 1:
        k += 1
        r /= k
    return k - 1

# Generate OEIS A085302
def generate_A085302(n_max):
    primes = generate_primes(n_max)
    sequence = []
    for n in range(1, n_max+1):
        n_prim = primorial(n, primes)
        if n == 1:
            a_n = 2  # first term explicitly set
        else:
            a_n = fn(n_prim) + 1
        sequence.append(a_n)
    return sequence

# Example usage
n_max = 50
a085302 = generate_A085302(n_max)
print("OEIS A085302 sequence (first 50 terms):")
print(a085302)
