import math

# --------------------------
# A052940
# --------------------------
def A052940(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        k += k + 1
        current += k//2
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A052940 = [1] + A052940(n)

print("Sequence A052940:")
print(seq_A052940)
