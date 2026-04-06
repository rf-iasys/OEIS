import math

# --------------------------
# A123121
# --------------------------
def A123121(n):
    marked = []
    current = 1
    k = 4

    while len(marked) < n:
        k += k + current//(2*k)
        current += k + 1
        marked.append(k-1)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

# Generate A123121 sequence.
seq_A123121 = [1,3] + A123121(n)

print("Sequence A123121:")
print(seq_A123121)
