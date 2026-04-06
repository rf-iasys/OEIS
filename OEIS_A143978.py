import math

# --------------------------
# A143978
# --------------------------
def A143978(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += current - 2*k//current
        current += 2
        marked.append(k+1)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 1000

seq_A143978 = A143978(n)

print("Sequence A143978:")
print(seq_A143978)
