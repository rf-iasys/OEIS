import math

# --------------------------
# A000244
# --------------------------
def A000244(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + k*current
        current += current//(k**2)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A000244 = A000244(n)

print("Sequence A000244:")
print(seq_A000244)
