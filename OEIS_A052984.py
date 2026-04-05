import math

# --------------------------
# A052984
# --------------------------
def A052984(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + current
        current += math.floor(current/k) + 2*k

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A052984 = A052984(n)

print("Sequence A052984:")
print(seq_A052984)
