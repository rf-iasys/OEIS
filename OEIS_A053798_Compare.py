import math

# --------------------------
# A053798 Sieve
# --------------------------
def A053798(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n - 1:  # subtract 1 to account for prepended first term
        marked.append(2*current)
        k += int(current/(k+1))
        current += k

    return [1] + marked  # prepend first OEIS term

# --------------------------
# A049347 periodic pattern
# --------------------------
def A049347(n):
    pattern = [1, -1, 0]
    if n < 0:
        return 0
    return pattern[n % 3]

# --------------------------
# A053798 formula-based generator
# --------------------------
def A053798_formula(n_terms):
    seq = []
    for n in range(n_terms):
        val = (n*(n**2 + 15) + 2*A049347(n-1)) // 9
        seq.append(val)
    if n_terms > 0:
        seq[0] = 1  # correct first term
    return seq

# --------------------------
# Compare the two sequences
# --------------------------
def compare_sequences(n_terms):
    seq_sieve = A053798(n_terms)
    seq_formula = A053798_formula(n_terms)

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
