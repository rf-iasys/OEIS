import math

# --------------------------
# A025192
# --------------------------
def A025192(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += current//2 + k//2
        current += 2*k
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 200

seq_A025192 = A025192(n+1)

print("Sequence A025192:")
print(seq_A025192)
