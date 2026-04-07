import math

# --------------------------
# A047926
# --------------------------
def A047926(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += 2*k - current
        current += 1
        marked.append(k-1)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A047926 = A047926(n+1)

print("Sequence A047926:")
print(seq_A047926)
