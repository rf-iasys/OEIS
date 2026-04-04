import math

# --------------------------
# Your sieve
# --------------------------
def sieve_simulation(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append(current)
        k += math.floor((2*current) / k)**2
        current += k

    return marked

# --------------------------
# 2*(a(n+1) - a(n))
# --------------------------
def doubled_differences(seq):
    return [2*(seq[i+1] - seq[i]) for i in range(len(seq)-1)]

# --------------------------
# A271996 exact formula
# OFFSET = 2
# --------------------------
def A271996_formula(n_terms):
    seq = []
    for n in range(2, n_terms + 2):  # start at n=2
        if n % 2 == 0:
            val = (n**3 + 6*n**2 + 14*n - 24) // 6
        else:
            val = (n**3 + 6*n**2 + 11*n - 30) // 6
        seq.append(val)
    return seq

# --------------------------
# Compare sequences
# --------------------------
def compare_sequences(n_terms):
    sieve_seq = sieve_simulation(n_terms + 1)  # need one extra for diff
    diffs = doubled_differences(sieve_seq)

    ref = A271996_formula(n_terms)

    all_match = True
    for i in range(n_terms):
        if diffs[i] != ref[i]:
            print(f"Mismatch at term {i+2}: sieve={diffs[i]}, A271996={ref[i]}")
            all_match = False

    if all_match:
        print(f"All {n_terms} terms match perfectly!")
    else:
        print("Some terms do not match.")

# --------------------------
# Run comparison for first 100000 terms
# --------------------------
compare_sequences(100000)
