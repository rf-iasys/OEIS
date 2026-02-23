import math
from collections import defaultdict

# ========================
# ===== FUNCTIONS ========
# ========================

def a080827(n):
    """OEIS A080827: ceil((n^2 + 1)/2)"""
    return math.ceil((n**2 + 1)/2)

def compute_n_end_from_k(k_max):
    return max(2 * a080827(k) for k in range(4, k_max+1))

# ----- Memory-optimized version for irregular prefixes only -----
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
        # Skip columns 1..3 and last column k_max
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

# ========================
# ===== PARAMETERS =======
# ========================

k_max = 200
n_end = compute_n_end_from_k(k_max)

# ----- Compute results -----
max_delta_mem = compute_max_delta_memopt(n_end)
irregular_prefixes = extract_irregular_prefixes(max_delta_mem, k_max)

# ========================
# ===== EXTRACT L4, L5, L6... =======
# ========================

# Initialize a dictionary to store L4, L5, L6, ...
L_values = {}

# Loop through each "n" from 1 to the maximum column
max_len = max(len(irregular_prefixes[k]) for k in irregular_prefixes)  # max length of any list

for n in range(max_len):
    L_values[f"L{n+4}"] = []  # Start from L4

    for k in range(4, k_max):  # Start from Column 4
        if k in irregular_prefixes and len(irregular_prefixes[k]) > n:
            L_values[f"L{n+4}"].append(irregular_prefixes[k][n])  # Extract nth element (0-indexed)

# ========================
# ===== SAVE TO TXT =======
# ========================

output_file = "1_15_L.txt"
with open(output_file, "w") as f:
    for n in range(4, k_max):
        if f"L{n}" in L_values:
            f.write(f"{f'L{n}'}: {L_values[f'L{n}']}\n")

print(f"✅ L4 to L{k_max-1} values saved to '{output_file}'")
