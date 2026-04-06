import math

# --------------------------
# A083329
# --------------------------
def A083329(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + current//(k+1)
        current += k

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 1000

# Generate A083329 sequence.
seq_A083329 = A083329(n+1)

print("Sequence A083329:")
print(seq_A083329)
