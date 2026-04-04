import math

# --------------------------
# Sieve simulation
# --------------------------
def sieve_simulation(n):
    marked = []
    current = 1
    k = 2
    while len(marked) < n:
        marked.append(current)
        k += math.floor(current / (k + 2))
        current += k
    return marked

# --------------------------
# Transform coefficients: Sn(z) * (1-z)/(1+z)
# --------------------------
def transform_coefficients(seq):
    """
    Given a sequence seq[0], seq[1], ... returns
    b_n = coefficient of z^n in seq * (1-z)/(1+z)
    """
    n_terms = len(seq)
    transformed = []
    for n in range(n_terms):
        val = 0
        for k in range(n+1):
            sign = (-1)**k
            multiplier = 2 if k > 0 else 1
            val += seq[n - k] * sign * multiplier
        transformed.append(val)
    return transformed

# --------------------------
# A094909 formula using integer partitions
# --------------------------
def partitions_exact_k(n, k):
    if n < k or k == 0:
        return 0
    if k == 1 or n == k:
        return 1
    return partitions_exact_k(n-1, k-1) + partitions_exact_k(n-k, k)

def A094909_formula(n_terms):
    seq = []
    for n in range(n_terms):
        p2 = partitions_exact_k(n-2, 2) if n >= 2 else 0
        p3 = partitions_exact_k(n-3, 3) if n >= 3 else 0
        seq.append(1 + p2 + p3)
    return seq

# --------------------------
# Compare sequences
# --------------------------
def compare_sieve_to_A094909(n_terms):
    sieve_seq = sieve_simulation(n_terms)
    transformed_seq = transform_coefficients(sieve_seq)
    formula_seq = A094909_formula(n_terms + OFFSET)  # include offset

    all_match = True
    #print("Index | Transformed Sieve | A094909")
    for i in range(n_terms):
        t = transformed_seq[i]
        f = formula_seq[i + OFFSET]  # shift by OFFSET
        #print(f"{i:3d}   | {t:5d}            | {f:5d}")
        if t != f:
            all_match = False

    if all_match:
        print(f"\nAll {n_terms} terms match perfectly!")
    else:
        print("\nSome terms differ.")

OFFSET = 1  # shift A094909 to align with transformed sieve

# --------------------------
# Run comparison for first 1000 terms
# --------------------------
compare_sieve_to_A094909(1000)
