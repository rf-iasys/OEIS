import math

# --------------------------
# A052913
# --------------------------
def A052913(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + current + 1
        current += 2*k

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A052913 = A052913(n+1)

print("Sequence A052913:")
print(seq_A052913)
