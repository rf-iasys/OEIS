import math

# --------------------------
# A084215
# --------------------------
def A084215(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + current//(3*k)
        current += k + 3

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

# Generate A084215 sequence.
seq_A084215 = A084215(n+1)

print("Sequence A084215:")
print(seq_A084215)
