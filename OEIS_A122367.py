import math

# --------------------------
# A122367
# --------------------------
def A122367(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k//2)
        k += current - k//2
        current += current + k//2

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 1000

# Generate A122367 sequence.
seq_A122367 = A122367(n+2)

print("Sequence A122367:")
print(seq_A122367)
