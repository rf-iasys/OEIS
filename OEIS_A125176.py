import math

# --------------------------
# A125176
# --------------------------
def A125176(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += k + current//k
        current += k//current
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A125176 = [1] + A125176(n-1)

print("Sequence A125176:")
print(seq_A125176)
