# --------------------------
# OEIS formula
# --------------------------
def A116453_oeis(n):
    return 5 if n == 1 else 9 * 2**(n - 2)

# --------------------------
# A116453 recurrence
# --------------------------
def A116453_recurrence(n_terms):
    marked = []
    current = 1
    k = 2
    while len(marked) < n_terms:
        k += k + current // k
        current += k // current
        marked.append(k)
    # Add 1 to first term.
    if marked:
        marked[0] += 1
    return marked

# --------------------------
# Test first n terms
# --------------------------
n = 100000

# Generate OEIS sequence
seq_oeis = [A116453_oeis(i+1) for i in range(n)]

# Generate recurrence sequence
seq_recurrence = A116453_recurrence(n)

# Compare sequences
matches = [seq_oeis[i] == seq_recurrence[i] for i in range(n)]
all_match = all(matches)

print("Do all terms match?", all_match)
if not all_match:
    # Show first mismatch
    for i, m in enumerate(matches):
        if not m:
            print(f"Mismatch at n={i+1}: OEIS={seq_oeis[i]}, Recurrence={seq_recurrence[i]}")
            break
