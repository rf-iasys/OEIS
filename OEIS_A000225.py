import math

# --------------------------
# A000225
# --------------------------
def A000225(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += k + 1
        current += k//2
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A000225 = [0,1] + A000225(n-1)

print("Sequence A000225:")
print(seq_A000225)
