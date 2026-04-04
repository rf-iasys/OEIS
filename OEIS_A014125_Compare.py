import math

# --------------------------
# Your sieve-style generator for A014125
# --------------------------
def sieve_A014125(n):
    marked = []
    current = 1
    k = 1  # adjusted to match offsets

    while len(marked) < n:
        marked.append(current)
        k += math.floor(current / k)
        current += k  # advance by how many have been marked

    return marked

# --------------------------
# OEIS A014125 via A001400 bisection
# --------------------------
def A014125_exact(n_terms):
    # Generate A001400 (partitions into at most 4 parts)
    dp = [[0]*(2*n_terms+5) for _ in range(5)]
    for k in range(1, 5):
        dp[k][0] = 1
        for n in range(1, 2*n_terms+1):
            if n - k >= 0:
                dp[k][n] = dp[k-1][n] + dp[k][n-k]
            else:
                dp[k][n] = dp[k-1][n]
    a001400 = [dp[4][n] for n in range(1, 2*n_terms+1)]
    # Bisection: take every other term
    return [a001400[2*i] for i in range(n_terms)]

# --------------------------
# Compare the two sequences
# --------------------------
def compare_A014125(n_terms):
    seq_sieve = sieve_A014125(n_terms)
    seq_formula = A014125_exact(n_terms)

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
compare_A014125(100000)
