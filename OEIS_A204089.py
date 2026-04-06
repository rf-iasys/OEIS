import math

# --------------------------
# A204089
# --------------------------
def A204089(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + 2*current
        current += current//k + k//2

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 1000

seq_A204089 = A204089(n)

print("Sequence A204089:")
print(seq_A204089)
