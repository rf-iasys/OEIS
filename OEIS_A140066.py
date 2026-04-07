import math

# --------------------------
# A140066 - a(n) = (5*n^2 - 11*n + 8)/2.
# --------------------------
def A140066(n):
    marked = []
    current = 1
    k = 4

    while len(marked) < n:
        k += current - 4
        current += 5
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A140066 = A140066(n+1)

print("Sequence A140066:")
print(seq_A140066)
