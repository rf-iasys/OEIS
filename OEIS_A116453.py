import math

# --------------------------
# A116453
# --------------------------
def A116453(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        k += k + current//k
        current += k//current
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A116453 = A116453(n)

# Add 1 to the first term only
seq_A116453[0] += 1

print("Sequence A116453:")
print(seq_A116453)
