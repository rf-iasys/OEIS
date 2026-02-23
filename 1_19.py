import math
from collections import defaultdict

# ========================
# ===== FUNCTIONS ========
# ========================

def a080827(n):
    """Compute A080827(n) = ceiling((n^2 + 1)/2)"""
    return math.ceil((n**2 + 1)/2)


def compute_n_end_from_k(k_max):
    """
    Predict minimal n_end to fully generate columns up to k_max using A080827
    """
    n_end_list = []
    for k in range(4, k_max+1):
        a_n = 2 * a080827(k)
        n_end_list.append(a_n)
    return max(n_end_list)


def compute_max_delta(n_end):
    """
    Compute x = b^2 - a^2 for 0 <= a < b <= n_end,
    keeping only the maximum delta y = b-a per x.
    """
    max_delta = {}
    for a in range(n_end):
        for b in range(a+1, n_end - a + 1):
            x = b*b - a*a
            y = b - a
            if x not in max_delta or y > max_delta[x]:
                max_delta[x] = y
    return max_delta


def build_columns(max_delta):
    """
    Group x values by y (max delta) into columns.
    Each column is a list of x values.
    """
    grouped_by_y = defaultdict(list)
    for x, y in max_delta.items():
        grouped_by_y[y].append(x)

    max_len = max(len(xs) for xs in grouped_by_y.values())
    columns = []

    for i in range(max_len):
        col = []
        for y in sorted(grouped_by_y):
            xs = sorted(grouped_by_y[y])
            if i < len(xs):
                col.append(xs[i])
        columns.append(col)

    return columns


def analyze_columns(columns, k_max=None):
    """
    Analyze columns to find:
      - formula
      - stabilization point
      - run length
      - irregular prefix
    """
    results = {}
    if k_max is None:
        k_max = len(columns)

    for idx, col in enumerate(columns[:k_max], start=1):
        if idx <= 3:
            continue  # skip first 3 quadratic columns

        k = idx
        longest_run_start = None
        longest_run_end = None
        longest_len = 0
        current_start = None
        current_len = 0

        # Identify longest consecutive run matching the formula
        for i, x_val in enumerate(col):
            n = i + 1
            predicted = n * (n + 2*(k-1))
            if x_val == predicted:
                if current_start is None:
                    current_start = n
                current_len += 1
            else:
                if current_len > longest_len:
                    longest_len = current_len
                    longest_run_start = current_start
                    longest_run_end = current_start + current_len - 1
                current_start = None
                current_len = 0

        # Final run check
        if current_len > longest_len:
            longest_len = current_len
            longest_run_start = current_start
            longest_run_end = current_start + current_len - 1

        # Irregular prefix before stabilization
        irregular_prefix = [
            x_val for i, x_val in enumerate(col)
            if (i+1) < longest_run_start and (i+1)*(i+1 + 2*(k-1)) != x_val
        ]

        results[k] = {
            "formula": f"x = n(n + {2*(k-1)})",
            "stabilization_n": longest_run_start,
            "run_length": longest_len,
            "irregular_prefix": sorted(set(irregular_prefix))
        }

    return results


# ========================
# ===== PARAMETERS =======
# ========================

k_max = 40           # Maximum column number to analyze

# ========================
# ===== COMPUTE ========
# ========================

# Step 1: Compute n_end needed
n_end_required = compute_n_end_from_k(k_max)
print(f"Calculated n_end to fully generate columns up to k={k_max}: {n_end_required}")

# Step 2: Compute max_delta and build columns
max_delta = compute_max_delta(n_end_required)
columns = build_columns(max_delta)

# Step 3: Analyze columns
sequences = analyze_columns(columns, k_max=k_max)

# ========================
# ===== REPORT ==========
# ========================

print("\n===== COLUMN SEQUENCES =====")
for k, info in sequences.items():
    print("\n" + "-"*50)
    print(f"Column {k}")
    print("-"*50)
    print(f"Formula       : {info['formula']}")
    print(f"Stabilizes at : n = {info['stabilization_n']}")
    print(f"Run length    : {info['run_length']}")
    if info['irregular_prefix']:
        print(f"Irregular prefix (potential new OEIS sequence):")
        print(info['irregular_prefix'])
    else:
        print("No irregular values before stabilization.")
