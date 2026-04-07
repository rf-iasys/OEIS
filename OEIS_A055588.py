import math

# --------------------------
# A055588 - a(n) = 3*a(n-1) - a(n-2) - 1 with a(0) = 1 and a(1) = 2.
# --------------------------
def A055588(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += current - 1
        current += k
        marked.append(current-k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A055588 = A055588(n+1)

print("Sequence A055588:")
print(seq_A055588)
