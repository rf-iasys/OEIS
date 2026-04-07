import math

# --------------------------
# A319196
# --------------------------
def A319196(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += current - 3*k
        current += current + 2*k
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

# Generate A319196 sequence.
seq_A319196 = [1] + A319196(n)

print("Sequence A319196:")
print(seq_A319196)
