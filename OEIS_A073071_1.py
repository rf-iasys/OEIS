import math
import requests

# -----------------------------
# Load OEIS b-file data
# -----------------------------
def load_oeis_data(url: str) -> dict[int, int]:
    """
    Loads OEIS b-file data from a URL.
    Returns a dict mapping OEIS value -> index in the sequence.
    Raises RuntimeError if fetch fails.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception:
        raise RuntimeError("Failed to fetch OEIS data (offline or URL unreachable)")

    lines = response.text.splitlines()
    oeis_data = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            index, value = line.split()
            index = int(index)
            value = int(value)
            if value not in oeis_data:
                oeis_data[value] = index
        except ValueError:
            continue
    return oeis_data

# Load OEIS A073071 data
oeis_url = "https://oeis.org/A073071/b073071.txt"
oeis_dict = load_oeis_data(oeis_url)

# -----------------------------
# Primes sieve
# -----------------------------
def primes_up_to(m):
    sieve = [True]*(m+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(m**0.5)+1):
        if sieve[i]:
            for j in range(i*i, m+1, i):
                sieve[j] = False
    return [i for i, is_p in enumerate(sieve) if is_p]

primes_list = primes_up_to(10000)
primes_set = set(primes_list)

# -----------------------------
# Logarithmic primorial (cached)
# -----------------------------
primorial_log_cache = {}
def log_primorial(x):
    if x in primorial_log_cache:
        return primorial_log_cache[x]
    # Only use primes <= x
    val = sum(math.log(p) for p in primes_list if p <= x)
    primorial_log_cache[x] = val
    return val

def log_sum_exp(log_a, log_b):
    m = max(log_a, log_b)
    return m + math.log(1 + math.exp(-abs(log_a - log_b)))

# -----------------------------
# Compute first n for given k using log-space sum of primorials
# -----------------------------
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

# -----------------------------
# Build first_n map for k = 1..10000
# -----------------------------
k_max = 10000
first_n_map = {}
for k in range(1, k_max+1):
    n = find_first_n_sum(k, n_max=10000)
    if n is None:
        continue
    if n not in first_n_map:
        first_n_map[n] = []
    first_n_map[n].append(k)

# -----------------------------
# Extract n sequence and check first k primes
# -----------------------------
n_sequence = []
all_first_k_prime = True
for n in sorted(first_n_map.keys()):
    ks = first_n_map[n]
    first_k = ks[0]
    n_sequence.append(n)
    if first_k != 1 and first_k not in primes_set:
        print(f"WARNING: first k = {first_k} for first n = {n} is not prime!")
        all_first_k_prime = False

print("\n=== Computed n sequence ===")
print(n_sequence)

print("\n=== First k prime check ===")
if all_first_k_prime:
    print("All first k values are prime (or 1). ✅")
else:
    print("Some first k values are NOT prime. ❌")

# -----------------------------
# Compare with OEIS A073071
# -----------------------------
matches = []
for n in n_sequence:
    if n in oeis_dict:
        matches.append(n)

print(f"\nMatching values with OEIS A073071: {len(matches)} out of {len(n_sequence)}")
print(f"Comparisons:")
for i, n in enumerate(n_sequence):
    oeis_index = oeis_dict.get(n, None)
    match = oeis_index is not None
    print(f"{i+1:3d}: computed n = {n:5d}, OEIS index = {oeis_index}, match = {match}")
