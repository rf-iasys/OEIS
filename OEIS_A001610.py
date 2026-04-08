import math

# --------------------------
# A001610 a(n) = a(n-1) + a(n-2) + 1, with a(0) = 0 and a(1) = 2
# --------------------------
def A001610(n):
    marked = []
    k1 = 1
    k2 = 1

    while len(marked) < n:
        k1 += k2 - 2*k1
        k2 += k1 + 1
        marked.append(k1)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A001610 = A001610(n+1)[:n+1]

print("Sequence A001610 :")
print(seq_A001610)
