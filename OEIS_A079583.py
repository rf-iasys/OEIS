import math

# --------------------------
# A079583
# --------------------------
def A079583(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + current
        current += math.floor(current/k) + 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A079583 = A079583(n)

print("Sequence A079583:")
print(seq_A079583)
