import math

# --------------------------
# A007070
# --------------------------
def A007070(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + 2*current
        current += k//2 - current//k

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A007070 = A007070(n)

print("Sequence A007070:")
print(seq_A007070)
