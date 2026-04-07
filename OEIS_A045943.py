import math

# --------------------------
# A045943 - Triangular matchstick numbers: a(n) = 3*n*(n+1)/2
# --------------------------
def A045943(n):
    marked = []
    current = 1
    k = 0

    while len(marked) < n:
        k += current - 1
        current += 3
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A045943 = A045943(n+1)

print("Sequence A045943:")
print(seq_A045943)
