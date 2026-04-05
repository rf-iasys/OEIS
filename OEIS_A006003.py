import math

# --------------------------
# A006003
# --------------------------
def A006003(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(current)
        k += 1
        current += math.floor(current/k) + k**2

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A006003 = A006003(n)

print("Sequence A006003:")
print(seq_A006003)
