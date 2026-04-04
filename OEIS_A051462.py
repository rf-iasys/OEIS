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
# --------------------------
def even_terms(seq):
    # indices 1,3,5,... → a(2), a(4), a(6), ...
    return seq[1::2]

# --------------------------
# Example
# --------------------------
seq = sieve_simulation(50)
even_seq = even_terms(seq)

print("Full sequence:")
print(seq)

print("\nEven-indexed terms (a(2), a(4), ...):")
print(even_seq)
