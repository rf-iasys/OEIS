import math

# --------------------------
# A007052
# --------------------------
def A007052(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + current
        current += math.floor(current/k) + k

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A007052 = A007052(n)

print("Sequence A007052:")
print(seq_A007052)
