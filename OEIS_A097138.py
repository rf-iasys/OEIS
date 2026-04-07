import math

# --------------------------
# A097138
# --------------------------
def A097138(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k-1)
        k += current//3 + k
        current += current + 3*k

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

# Generate A097138 sequence.
seq_A097138 = [0] + A097138(n)

print("Sequence A097138:")
print(seq_A097138)
