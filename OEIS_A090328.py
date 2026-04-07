import math

# --------------------------
# A090328
# --------------------------
def A090328(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append(k-1)
        k += 2*k - current
        current += 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A090328 = A090328(n+1)

print("Sequence A090328:")
print(seq_A090328)
