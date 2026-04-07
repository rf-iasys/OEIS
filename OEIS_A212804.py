import math

# --------------------------
# A212804 Expansion of (1 - x)/(1 - x - x^2)
# --------------------------
def A212804(n):
    marked = []
    k1 = 2
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
n = 1000

seq_A212804 = A212804(n+1)[:n+1]

print("Sequence A212804 - Expansion of (1 - x)/(1 - x - x^2):")
print(seq_A212804)
