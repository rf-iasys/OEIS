import math

# --------------------------
# Your sieve-style generator
# --------------------------
def sieve_simulation(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n - 3:  # subtract 3 for initial terms
        marked.append(current + 1)
        k += math.floor(current / (k - 1))
        current += k  # advance by how many have been marked

    # Prepend first three OEIS terms
    return [0, 0, 1] + marked

# --------------------------
# OEIS formula-based generator
# --------------------------
def A393083_exact(n_terms):
    seq = []
    for n in range(1, n_terms + 1):
        if n == 1 or n == 2:
            seq.append(0)
        elif n == 3:
            seq.append(1)
        else:
            val = (-54 - 9 * n + 3 * n**3 + 4 * math.sqrt(3) * math.sin(2 * math.pi * n / 3)) / 54
            seq.append(int(round(val)))
    return seq

# --------------------------
# Compare the two sequences
# --------------------------
def compare_sequences(n_terms):
    seq_sieve = sieve_simulation(n_terms)
    seq_formula = A393083_exact(n_terms)

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
compare_sequences(100000)
