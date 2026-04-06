import math

# --------------------------
# A055819
# --------------------------
def A055819(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += current - k//2
        current += current + k//2

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

# Generate A055819 sequence.
seq_A055819 = A055819(n+1)

print("Sequence A055819:")
print(seq_A055819)
