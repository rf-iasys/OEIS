import math

# --------------------------
# Sieve-style generator
# --------------------------
def sieve_A004006(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(current)
        k += math.floor((3*current)/(k+2))
        current += k

    return marked

# --------------------------
# OEIS formula-based generator
# --------------------------
def A004006_exact(n_terms):
    return [n*(n**2 + 5)//6 for n in range(1, n_terms+1)]

# --------------------------
# Compare sequences
# --------------------------
def compare_A004006(n_terms):
    seq_sieve = sieve_A004006(n_terms)
    seq_formula = A004006_exact(n_terms)

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
compare_A004006(100000)
