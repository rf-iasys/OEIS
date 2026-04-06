import math

# --------------------------
# A056236
# --------------------------
def A056236(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k+1)
        k += k + current
        current += k + 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 1000

seq_A056236 = A056236(n+1)

print("Sequence A056236:")
print(seq_A056236)
