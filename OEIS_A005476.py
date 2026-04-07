import math

# --------------------------
# A005476 - a(n) = n*(5*n - 1)/2
# --------------------------
def A005476(n):
    marked = []
    current = 1
    k = 3

    while len(marked) < n:
        k += current - 4
        current += 5
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A005476 = A005476(n+1)

print("Sequence A005476:")
print(seq_A005476)
