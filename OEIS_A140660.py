import math

# --------------------------
# A140660
# --------------------------
def A140660(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        k += current//2 + k
        current += current + 2*k
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

# Generate A140660 sequence.
seq_A140660 = A140660(n+1)

print("Sequence A140660:")
print(seq_A140660)
