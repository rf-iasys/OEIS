import math

# --------------------------
# Your sieve-style generator for A000125
# --------------------------
def sieve_simulation_A000125(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(current)
        k += math.floor((3 * current) / (k + 3))
        current += k  # advance by how many have been marked

    return marked

# --------------------------
# OEIS formula-based generator (Cake numbers)
# a(n) = C(n+1,3) + n + 1
# --------------------------
def A000125_exact(n_terms):
    seq = []
    for n in range(n_terms):
        val = (n + 1) * n * (n - 1) // 6 + n + 1  # integer formula
        seq.append(val)
    return seq

# --------------------------
# Compare the two sequences
# --------------------------
def compare_sequences_A000125(n_terms):
    seq_sieve = sieve_simulation_A000125(n_terms)
    seq_formula = A000125_exact(n_terms)

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
# Run comparison for first 100000 terms
# --------------------------
compare_sequences_A000125(100000)
