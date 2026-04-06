import math

# --------------------------
# A153893
# --------------------------
def A153893(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += k + current//(2*k)
        current += k + 2
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 1000

# Generate A153893 sequence.
seq_A153893 = A153893(n+1)

print("Sequence A153893:")
print(seq_A153893)
