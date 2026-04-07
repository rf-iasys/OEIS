import math

# --------------------------
# A164039
# --------------------------
def A164039(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += 2*k - current
        current += 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 1000

seq_A164039 = A164039(n+1)

print("Sequence A164039:")
print(seq_A164039)
