import math

# --------------------------
# A293007
# --------------------------
def A293007(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += current - 2*k
        current += current + k
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

# Generate A293007 sequence.
seq_A293007 = [0] + A293007(n)

print("Sequence A293007:")
print(seq_A293007)
