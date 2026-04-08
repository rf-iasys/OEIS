import math

# --------------------------
# A103453 a(n) = 0^n + 3^n - 1
# --------------------------
def A103453(n):
    marked = []
    k1 = 1
    k2 = 1

    while len(marked) < n:
        marked.append(k1)
        k1 += 2*k2 - k1
        k2 += k1 + 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A103453 = A103453(n+1)[:n+1]

print("Sequence A103453 :")
print(seq_A103453)
