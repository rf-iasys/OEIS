import math

# --------------------------
# A083329
# --------------------------
def A083329(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        k += k + current//(2*k)
        current += k + 1
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 1000

# Generate a few extra to account for dropping the first 2
seq_A083329_full = A083329(n + 3)

# Exclude the first 2 items
seq_A083329 = seq_A083329_full[2:]

print("Sequence A083329 (without first 2 items):")
print(seq_A083329)
