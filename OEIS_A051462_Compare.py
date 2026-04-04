import math

# --------------------------
# Your sieve
# --------------------------
def sieve_simulation(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(current + 1)
        k += math.floor((current + 1) / (k + 1))
        current += k

    return marked

# --------------------------
# Extract even-indexed terms
# a(2), a(4), a(6), ...
# --------------------------
def even_terms(seq):
    return seq[1::2]

# --------------------------
# OEIS A051462 formula
# a(n) = (1 + 2*(2*n + 1)*(n^2 + n + 4) - (n mod 3)) / 9
# --------------------------
def A051462_formula(n_terms):
    seq = []
    for n in range(n_terms):
        val = (1 + 2*(2*n + 1)*(n**2 + n + 4) - (n % 3)) // 9
        seq.append(val)
    return seq

# --------------------------
# Compare sequences
# --------------------------
def compare_sequences(n_terms):
    seq = sieve_simulation(2*n_terms + 10)  # enough terms
    even_seq = even_terms(seq)

    ref = A051462_formula(n_terms + 1)  # +1 for offset

    all_match = True
    for i in range(n_terms):
        if even_seq[i] != ref[i+1]:  # shift by +1
            print(f"Mismatch at term {i+1}: sieve={even_seq[i]}, formula={ref[i+1]}")
            all_match = False

    if all_match:
        print(f"All {n_terms} terms match perfectly!")
    else:
        print("Some terms do not match.")

# --------------------------
# Run test
# --------------------------
compare_sequences(100000000)
