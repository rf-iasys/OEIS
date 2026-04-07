import math

# --------------------------
# A054135
# --------------------------
def A054135(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append(k-1)
        k += k + current//(k+1) - 1
        current += k - 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A054135 = A054135(n+1)

print("Sequence A054135:")
print(seq_A054135)
