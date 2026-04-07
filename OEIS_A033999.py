import math

# --------------------------
# A033999
# --------------------------
def A033999(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += current - 3*k
        current += current + 3*k
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

# Generate A033999 sequence.
seq_A033999 = [1] + A033999(n)

print("Sequence A033999:")
print(seq_A033999)
