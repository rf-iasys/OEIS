import math

# --------------------------
# A034472
# --------------------------
def A034472(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append(k)
        k += current + k//2
        current += k - 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A034472 = A034472(n+1)

print("Sequence A034472:")
print(seq_A034472)
