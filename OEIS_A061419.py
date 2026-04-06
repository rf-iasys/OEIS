import math

# --------------------------
# A061419
# --------------------------
def A061419(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k - k//2
        current += k + 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 500

seq_A061419 = A061419(n-1)

print("Sequence A061419:")
print(seq_A061419)
