import math
from collections import defaultdict
import requests
import time

# ========================
# ===== FUNCTIONS ========
# ========================

def a080827(n):
    """OEIS A080827: ceil((n^2 + 1)/2)"""
    return math.ceil((n**2 + 1)/2)

def compute_n_end_from_k(k_max):
    return max(2 * a080827(k) for k in range(4, k_max+1))

def compute_max_delta_memopt(n_end):
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
# ===== OEIS QUERY =======
# ========================

def match_to_oeis(sequence, max_terms=25, max_results=1, pause=10.0):
    if not sequence:
        return []
    query = ','.join(map(str, sequence[:max_terms]))
    url = f"https://oeis.org/search?fmt=json&q={query}"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        print(f"⚠️ Network error querying OEIS: {e}")
        return []
    except ValueError as e:
        print(f"⚠️ Failed to parse JSON from OEIS: {e}")
        return []

    if isinstance(data, dict):
        results = data.get('results', [])
    elif isinstance(data, list):
        results = data
    else:
        results = []

    matches = []
    for r in results[:max_results]:
        number = r.get('number')
        name = r.get('name')
        if number and name:
            matches.append((number, name))
    time.sleep(pause)
    return matches

# ========================
# ===== PARAMETERS =======
# ========================

k_max = 100
n_end = compute_n_end_from_k(k_max)
max_delta_mem = compute_max_delta_memopt(n_end)
irregular_prefixes = extract_irregular_prefixes(max_delta_mem, k_max)

# ========================
# ===== EXTRACT Lx =======
# ========================

L_values = {}
max_len = max(len(irregular_prefixes[k]) for k in irregular_prefixes)

for n in range(max_len):
    L_values[f"L{n+4}"] = []
    for k in range(4, k_max):
        if k in irregular_prefixes and len(irregular_prefixes[k]) > n:
            L_values[f"L{n+4}"].append(irregular_prefixes[k][n])

L_split = {}
for key, seq in L_values.items():
    left, right = split_on_strict_decrease(seq)
    L_split[key] = {"left": left, "right": right}

# ========================
# ===== SAVE TO TXT =======
# ========================

output_file = "1_17_L_OEIS.txt"
with open(output_file, "w") as f:
    for n in range(4, k_max):
        key = f"L{n}"
        if key in L_split:
            parts = L_split[key]
            f.write(f"{key}:1 {parts['left']}\n")
            if parts['right']:
                # Query OEIS for right part
                matches = match_to_oeis(parts['right'])
                oeis_str = f" -> OEIS match: {matches[0][0]} {matches[0][1]}" if matches else ""
                f.write(f"{key}:2 {parts['right']}{oeis_str}\n")
            f.write("\n")

print(f"✅ L4 to L{k_max-1} split and OEIS matches saved to '{output_file}'")
