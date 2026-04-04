import math

# --------------------------
# Your sieve-style generator for A002623
# --------------------------
def sieve_A002623(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(current)
        k += math.floor((3 * current) / (k * 2))
        current += k

    return marked

# --------------------------
# OEIS formula-based generator (expansion of 1/((1-x)^4*(1+x)))
# --------------------------
def A002623_formula(n_terms):
    seq = []
    for n in range(n_terms):
        val = sum((-1)**k * math.comb(n - k + 3, 3) for k in range(n + 1) if n - k >= 0)
        seq.append(val)
    return seq

# --------------------------
# Compare sequences
# --------------------------
def compare_A002623(n_terms):
    seq_sieve = sieve_A002623(n_terms)
    seq_formula = A002623_formula(n_terms)

    all_match = True
    for i, (s, f) in enumerate(zip(seq_sieve, seq_formula), start=1):
        if s != f:
            print(f"Mismatch at term {i}: sieve={s}, formula={f}")
            all_match = False

    if all_match:
        print(f"All {n_terms} terms match perfectly!")
    else:
        print("Some terms do not match.")

# --------------------------
# Example: compare first 100000 terms
# --------------------------
compare_A002623(100000)
