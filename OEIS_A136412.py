import math

# --------------------------
# A136412
# --------------------------
def A136412(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += current//2 + k
        current += current + 2*k
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

# Generate A136412 sequence.
seq_A136412 = A136412(n+1)

print("Sequence A136412:")
print(seq_A136412)
