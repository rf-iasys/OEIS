import math

# --------------------------
# A000032 Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1) = 1
# --------------------------
def A000032(n):
    marked = []
    k1 = 3
    k2 = 1

    while len(marked) < n:
        k1 += k2 - 2
        k2 += k1
        marked.append(k1)
        marked.append(k2 - 2)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A000032 = A000032(n+1)[:n+1]

print("Sequence A000032 - Lucas numbers beginning at 2: L(n):")
print(seq_A000032)
