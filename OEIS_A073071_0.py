import math

# Sieve to compute primes up to m
def primes_up_to(m):
    sieve = [True] * (m+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(m**0.5)+1):
        if sieve[i]:
            for j in range(i*i, m+1, i):
                sieve[j] = False
    return [i for i in range(2, m+1) if sieve[i]]

# Compute log of primorial of x (cached)
primorial_log_cache = {}
def log_primorial(x):
    if x in primorial_log_cache:
        return primorial_log_cache[x]
    primes = primes_up_to(x)
    val = sum(math.log(p) for p in primes)
    primorial_log_cache[x] = val
    return val

# Numerically stable log(a + b)
def log_sum_exp(log_a, log_b):
    m = max(log_a, log_b)
    return m + math.log(1 + math.exp(-abs(log_a - log_b)))

# Find first n for given k using log-space sum of primorials
def find_first_n_sum(k, n_max=10000):
    log_fact = 0.0
    n = 1
    log_k_prim = log_primorial(k)
    while n <= n_max:
        if n > 1:
            log_fact += math.log(n)
        log_n_prim = log_primorial(n)
        log_sum = log_sum_exp(log_n_prim, log_k_prim)
        if log_fact >= log_sum:
            return n
        n += 1
    return None

# Build table: first n -> list of k
first_n_map = {}
k_max = 10000
for k in range(1, k_max+1):
    n = find_first_n_sum(k, n_max=10000)
    if n not in first_n_map:
        first_n_map[n] = []
    first_n_map[n].append(k)

# Print grouped by first n
for n in sorted(first_n_map.keys()):
    ks = ','.join(str(k) for k in first_n_map[n])
    print(f"first n = {n} -> k = {ks}")
