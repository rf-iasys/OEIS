import math

# --------------------------
# A008346 - a(n) = Fibonacci(n) + (-1)^n
# --------------------------
def A008346(n):
    marked = []
    k1 = 2
    k2 = 1
    k3 = 1

    while len(marked) < n:
        k1 += k2 - 2
        k2 += k1
        marked.append(k1-k3)
        marked.append(k2-k3)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A008346 = A008346(n+1)[1:]

print("Sequence A008346:")
print(seq_A008346)
