import math

# --------------------------
# A337300
# --------------------------
def A337300(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(current)
        k += 1
        current += math.floor(current/k) + k

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A337300 = A337300(n)

print("Sequence A337300:")
print(seq_A337300)
