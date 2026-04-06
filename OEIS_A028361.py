import math

# --------------------------
# A028361
# --------------------------
def A028361(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k*current
        current += current

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 50

seq_A028361 = A028361(n+1)

print("Sequence A028361:")
print(seq_A028361)
