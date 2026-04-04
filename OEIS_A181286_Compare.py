import math

# --------------------------
# Your new sieve-style generator
# --------------------------
def sieve_simulation_A181286(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(current)
        k += math.floor((2*current)/k)
        current += k

    return marked

# --------------------------
# OEIS formula-based generator (partial sums of floor(n^2/3))
# --------------------------
def A181286_exact(n_terms):
    seq = []
    total = 0
    for n in range(1, n_terms + 1):
        total += (n+1)**2 // 3  # floor division
        seq.append(total)
    return seq

# --------------------------
# Compare the two sequences
# --------------------------
def compare_sequences_A181286(n_terms):
    seq_sieve = sieve_simulation_A181286(n_terms)
    seq_formula = A181286_exact(n_terms)

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
compare_sequences_A181286(100000)
