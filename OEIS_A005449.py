import math

# --------------------------
# A005449 - Second pentagonal numbers: a(n) = n*(3*n + 1)/2
# --------------------------
def A005449(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += current - 2
        current += 3
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A005449 = A005449(n+1)

print("Sequence A005449:")
print(seq_A005449)
