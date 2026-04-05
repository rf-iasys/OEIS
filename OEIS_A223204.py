import math

# --------------------------
# A223204
# --------------------------
def A223204(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += k + current
        current += math.floor(current/k) + 6*k
        marked.append(3*k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 210

seq_A223204 = A223204(n)

print("Sequence A223204:")
print(seq_A223204)
