import math

# --------------------------
# A000325
# --------------------------
def A000325(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += (k**2)*current//(k**2)
        current += current + 1

    return [1] + marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A000325 = A000325(n)

print("Sequence A000325:")
print(seq_A000325)
