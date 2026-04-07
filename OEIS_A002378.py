import math

# --------------------------
# A002378 - Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)
# --------------------------
def A002378(n):
    marked = []
    current = 1
    k = 0

    while len(marked) < n:
        k += current - 1
        current += 2
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A002378 = A002378(n+1)

print("Sequence A002378:")
print(seq_A002378)
