import math

# --------------------------
# A146963
# --------------------------
def A146963(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + current
        current += math.floor(current/k) + 3*k

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 200

seq_A146963 = A146963(n)

print("Sequence A146963:")
print(seq_A146963)
