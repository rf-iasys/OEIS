import math

# --------------------------
# A000035
# --------------------------
def A000035(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += current - 2*k
        current += current//2 + k//2

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

# Generate A000035 sequence.
seq_A000035 = A000035(n)

print("Sequence A000035:")
print(seq_A000035)
