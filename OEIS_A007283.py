import math

# --------------------------
# A007283
# --------------------------
def A007283(n):
    marked = []
    current = 1
    k = 3

    while len(marked) < n:
        marked.append(k)
        k += k + current//(3*k)
        current += k + 3

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

# Generate A007283 sequence.
seq_A007283 = A007283(n+1)

print("Sequence A007283:")
print(seq_A007283)
