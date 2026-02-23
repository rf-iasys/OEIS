import math
from collections import defaultdict
import sympy  # For prime checks

# ========================
# ===== FUNCTIONS ========
# ========================

def a080827(n):
    """OEIS A080827: ceil((n^2 + 1)/2)"""
    return math.ceil((n**2 + 1)/2)

def compute_n_end_from_k(k_max):
    return max(2 * a080827(k) for k in range(4, k_max+1))

def compute_max_delta_memopt(n_end):
    """Memory-efficient computation of max_delta for irregular prefixes"""
    max_x = (n_end//2)**2
    max_delta = [0]*(max_x+1)
    for a in range(n_end//2):
        for b in range(a+1, (n_end - a + 1)//2):
            x = b*b - a*a
            y = b - a
            if y > max_delta[x]:
                max_delta[x] = y
    return max_delta

def extract_irregular_prefixes(max_delta, k_max):
    grouped_by_y = defaultdict(list)
    for x, y in enumerate(max_delta):
        if y > 0:
            grouped_by_y[y].append(x)

    sorted_ys = sorted(grouped_by_y)
    max_len = max(len(grouped_by_y[y]) for y in grouped_by_y)
    results = {}

    for i in range(max_len):
        k = i + 1
        if k <= 3 or k >= k_max:
            continue
        col = [grouped_by_y[y][i] for y in sorted_ys if i < len(grouped_by_y[y])]
        irregular_prefix = [
            x_val for idx, x_val in enumerate(col)
            if (idx + 1) * (idx + 1 + 2 * (k - 1)) != x_val
        ]
        if irregular_prefix:
            results[k] = irregular_prefix
    return results

def split_on_strict_decrease(L):
    """Splits list L into left/right based on strict decrease from right to left"""
    n = len(L)
    split_index = None
    for i in range(n-1, 0, -1):
        if L[i-1] >= L[i]:
            split_index = i
            break
    if split_index is None:
        return [], L
    return L[:split_index], L[split_index:]

# ========================
# ===== PRIME CHAIN CHECK =======
# ========================

def check_consecutive_prime_chain(L_split):
    """
    Checks Lx:2 sequences for consecutive prime multiple chains.
    Returns a dictionary of matches with details.
    """
    matches = {}
    for key, parts in L_split.items():
        seq = parts['right']
        if not seq or len(seq) < 2:
            continue

        last_val = seq[-1]
        prime_factors_last = sympy.factorint(last_val)
        largest_prime = max(prime_factors_last) if prime_factors_last else None
        if not largest_prime:
            continue
        k = last_val // largest_prime

        chain_valid = True
        current_prime = largest_prime
        for val in reversed(seq):
            expected = k * current_prime
            if val != expected:
                chain_valid = False
                break
            current_prime = sympy.prevprime(current_prime)

        if chain_valid:
            matches[key] = {
                "k": k,
                "prime_chain_end": largest_prime,
                "length": len(seq),
                "sequence": seq
            }
    return matches

# ========================
# ===== PARAMETERS =======
# ========================

k_max = 200
n_end = compute_n_end_from_k(k_max)

# ----- Compute results -----
max_delta_mem = compute_max_delta_memopt(n_end)
irregular_prefixes = extract_irregular_prefixes(max_delta_mem, k_max)

# ----- Extract L4, L5, ... -----
L_values = {}
max_len = max(len(irregular_prefixes[k]) for k in irregular_prefixes)
for n in range(max_len):
    L_values[f"L{n+4}"] = []
    for k in range(4, k_max):
        if k in irregular_prefixes and len(irregular_prefixes[k]) > n:
            L_values[f"L{n+4}"].append(irregular_prefixes[k][n])

# ----- Split sequences -----
L_split = {}
for key, seq in L_values.items():
    left, right = split_on_strict_decrease(seq)
    L_split[key] = {"left": left, "right": right}

# ----- Save to file -----
output_file = "1_18_L.txt"
with open(output_file, "w") as f:
    for n in range(4, k_max):
        key = f"L{n}"
        if key in L_split:
            parts = L_split[key]
            f.write(f"{key}:1 {parts['left']}\n")
            if parts['right']:
                f.write(f"{key}:2 {parts['right']}\n")
            f.write("\n")
print(f"✅ L4 to L{k_max-1} split into numbered parts saved to '{output_file}'")

# ----- Check for prime multiple chains -----
prime_chains = check_consecutive_prime_chain(L_split)
print("\n=== Lx:2 sequences forming consecutive prime multiples ===\n")
for key, info in prime_chains.items():
    print(f"{key}: Length={info['length']}, k={info['k']}, "
          f"Largest prime={info['prime_chain_end']}")
    print(f"Sequence: {info['sequence']}\n")
