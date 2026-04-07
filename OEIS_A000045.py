import math

# --------------------------
# A000045 Fibonacci(n)
# --------------------------
def A000045(n):
    marked = []
    k1 = 2
    k2 = 1

    while len(marked) < n:
        k1 += k2 - 2
        k2 += k1
        marked.append(k1)
        marked.append(k2 - 2)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A000045 = A000045(n+1)[1:]

print("Fibonacci sequence:")
print(seq_A000045)
