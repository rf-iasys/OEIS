import math
import requests

# -----------------------------
# Sieve to compute primes up to m
# -----------------------------
def primes_up_to(m):
    sieve = [True]*(m+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(m**0.5)+1):
        if sieve[i]:
            for j in range(i*i, m+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# -----------------------------
# Precompute log factorials and log primorials
# -----------------------------
def precompute_logs(n_max):
    primes = primes_up_to(n_max)
    log_fact = [0.0]
    log_prim = [0.0]
    prim_index = 0
    
    for n in range(1, n_max+1):
        log_fact.append(log_fact[-1] + math.log(n))
        if prim_index < len(primes) and primes[prim_index] == n:
            log_prim.append(log_prim[-1] + math.log(n))
            prim_index += 1
        else:
            log_prim.append(log_prim[-1])
    
    return log_fact, log_prim

# -----------------------------
# Compute minimal natural b and first n per new b
# -----------------------------
def first_n_per_new_b(log_fact, log_prim):
    first_n_list = []
    seen_b = set()
    
    for n in range(2, len(log_fact)):
        b = math.ceil(log_fact[n] - log_prim[n])
        if b not in seen_b:
            first_n_list.append((n, b))
            seen_b.add(b)
    
    return first_n_list

# -----------------------------
# Load OEIS b-file data
# -----------------------------
def load_oeis_data(url: str) -> set[int]:
    """
    Loads OEIS b-file data from a URL.
    Returns a set of sequence values.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception:
        raise RuntimeError("Failed to fetch OEIS data (offline or URL unreachable)")

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
# Parameters
# -----------------------------
n_max = 1000

# Precompute logs
log_fact, log_prim = precompute_logs(n_max)

# Compute first n per new minimal natural b
first_n_sequence = first_n_per_new_b(log_fact, log_prim)
n_list = [n for n, b in first_n_sequence]

# -----------------------------
# Compare with OEIS A065090 (not odd primes)
# -----------------------------
oeis_url = "https://oeis.org/A065090/b065090.txt"
oeis_data = load_oeis_data(oeis_url)

matches = [n for n in n_list if n in oeis_data]
mismatches = [n for n in n_list if n not in oeis_data]

# -----------------------------
# Print results
# -----------------------------
print("First n per new minimal natural b:")
print("n\tb")
for n, b in first_n_sequence:
    print(f"{n}\t{b}")

print("\nOEIS-style:")
print("n =", ", ".join(str(n) for n in n_list))
print("b =", ", ".join(str(b) for n, b in first_n_sequence))

print(f"\nNumber of matches with OEIS A065090: {len(matches)}")
if mismatches:
    print(f"Mismatches: {mismatches}")
else:
    print("No mismatches: your sequence perfectly matches OEIS A065090.")
