import math
import requests

# =============================
# Load OEIS b-file data
# =============================
def load_oeis_data(url: str) -> set[int]:
    """
    Loads OEIS b-file data from a URL.
    Returns a set of OEIS values (sequence numbers).
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception:
        raise RuntimeError(f"Failed to fetch OEIS data from {url}")

    lines = response.text.splitlines()
    oeis_data = set()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            index, value = line.split()
            value = int(value)
            oeis_data.add(value)
        except ValueError:
            continue
    return oeis_data

# -----------------------------
# Sieve to compute primes up to m
# -----------------------------
def primes_up_to(m):
    """
    Standard sieve of Eratosthenes.
    Returns all primes ≤ m.
    """
    sieve = [True] * (m+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(m**0.5)+1):
        if sieve[i]:
            for j in range(i*i, m+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# =============================
# Part 1: A065090 generation
# Formula: n! < n# * e^b
# =============================
def precompute_logs(n_max):
    """
    Precomputes log factorials and log primorials up to n_max.
    """
    primes = primes_up_to(n_max)
    log_fact = [0.0]   # log(0!) = 0
    log_prim = [0.0]   # log(0#) = 0
    prim_index = 0
    
    for n in range(1, n_max+1):
        log_fact.append(log_fact[-1] + math.log(n))
        if prim_index < len(primes) and primes[prim_index] == n:
            log_prim.append(log_prim[-1] + math.log(n))
            prim_index += 1
        else:
            log_prim.append(log_prim[-1])
    return log_fact, log_prim

def first_n_per_new_b(log_fact, log_prim):
    """
    For each n, computes minimal natural b satisfying:
        n! < n# * e^b  ->  b = ceil(log(n!) - log(n#))
    Returns list of first n for each new b.
    """
    first_n_list = []
    seen_b = set()
    for n in range(2, len(log_fact)):
        b = math.ceil(log_fact[n] - log_prim[n])
        if b not in seen_b:
            first_n_list.append((n, b))
            seen_b.add(b)
    return first_n_list

# =============================
# Part 2: A000040 generation
# Formula: n! >= n# + k#
# =============================
primorial_log_cache = {}
def log_primorial(x):
    """
    Returns log of primorial of x: log(x#)
    """
    if x in primorial_log_cache:
        return primorial_log_cache[x]
    primes = primes_up_to(x)
    val = sum(math.log(p) for p in primes)
    primorial_log_cache[x] = val
    return val

def log_sum_exp(log_a, log_b):
    """
    Stable computation of log(a + b) given log(a), log(b)
    """
    m = max(log_a, log_b)
    return m + math.log(1 + math.exp(-abs(log_a - log_b)))

def find_first_n_sum(k, n_max=10000):
    """
    For given k, finds first n such that:
        n! >= n# + k#
    """
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

# =============================
# Main execution
# =============================
n_max = 1000   # Adjust as needed
k_max = 1000

# --- Load OEIS data ---
oeis_non_odd_primes = load_oeis_data("https://oeis.org/A065090/b065090.txt")
oeis_primes = load_oeis_data("https://oeis.org/A000040/a000040.txt")

# --- Generate A065090 ---
log_fact, log_prim = precompute_logs(n_max)
first_n_sequence_A065090 = first_n_per_new_b(log_fact, log_prim)
n_list_A065090 = [n for n, b in first_n_sequence_A065090]

# --- Generate A000040 ---
first_n_map_A000040 = {}
for k in range(5, k_max+1):
    n = find_first_n_sum(k, n_max=n_max)
    if n not in first_n_map_A000040:
        first_n_map_A000040[n] = []
    first_n_map_A000040[n].append(k)

# =============================
# Comparisons
# =============================
# Compare A065090
matches_A065090 = [n for n in n_list_A065090 if n in oeis_non_odd_primes]
mismatches_A065090 = [n for n in n_list_A065090 if n not in oeis_non_odd_primes]

# Compare A000040 (first k only)
first_k_primes = [first_n_map_A000040[n][0] for n in sorted(first_n_map_A000040.keys()) if n >= 5]
matches_A000040 = [k for k in first_k_primes if k in oeis_primes]
mismatches_A000040 = [k for k in first_k_primes if k not in oeis_primes]

# =============================
# Print results
# =============================
print("=== A065090: Non-odd-primes (composite + 1,2) ===")
print("First n per new b:")
for n, b in first_n_sequence_A065090:
    print(f"n = {n}, b = {b}")
print(f"Matches OEIS A065090: {len(matches_A065090)}/{len(n_list_A065090)}")
if mismatches_A065090:
    print("Mismatches:", mismatches_A065090)
else:
    print("No mismatches ✅")

print("\n=== A000040: Primes via factorial >= n# + k# ===")
print("First k for each n (n >= 5):")
for n in sorted(first_n_map_A000040.keys()):
    if n < 5: continue
    first_k = first_n_map_A000040[n][0]
    status = "✅ prime" if first_k in oeis_primes else "❌ NOT prime"
    print(f"n = {n}, first k = {first_k} -> {status}")

print(f"Matches OEIS A000040: {len(matches_A000040)}/{len(first_k_primes)}")
if mismatches_A000040:
    print("Mismatches:", mismatches_A000040)
else:
    print("No mismatches ✅")
