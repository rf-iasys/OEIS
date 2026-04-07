import math

# --------------------------
# A001519
# --------------------------
def A001519(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append(k//2)
        k += current - k//2
        current += current + k//2

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 200

# Generate A001519 sequence.
seq_A001519 = A001519(n+1)

print("Sequence A001519:")
print(seq_A001519)
