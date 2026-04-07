import math

# --------------------------
# A056220 - a(n) = 2*n^2 - 1
# --------------------------
def A056220(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += current - 3
        current += 4
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A056220 = A056220(n+1)

print("Sequence A056220:")
print(seq_A056220)
