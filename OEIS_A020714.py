import math

# --------------------------
# A020714
# --------------------------
def A020714(n):
    marked = []
    current = 1
    k = 5

    while len(marked) < n:
        marked.append(k)
        k += k + current//(3*k)
        current += k

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

# Generate A020714 sequence.
seq_A020714 = A020714(n+1)

print("Sequence A020714:")
print(seq_A020714)
