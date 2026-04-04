import math

# --------------------------
# Main sieve
# --------------------------
def sieve_simulation(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += math.floor(current / (k + 1))
        current += k

    return marked

# --------------------------
# OEIS A008748 formula
# a(n) = 1 + floor(n(n+1)/6)
# --------------------------
def A008748_formula(n_terms):
    return [1 + (n*(n+1))//6 for n in range(n_terms)]

# --------------------------
# Compare sequences
# --------------------------
def compare_sequences(n_terms):
    seq_sieve = sieve_simulation(n_terms)
    seq_formula = A008748_formula(n_terms)

    all_match = True
    for i, (s, f) in enumerate(zip(seq_sieve, seq_formula), start=0):
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
compare_sequences(100000)  # adjust number of terms as needed
