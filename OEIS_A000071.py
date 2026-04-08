import math

# --------------------------
# A000071 a(n) = Fibonacci(n) - 1
# --------------------------
def A000071(n):
    marked = []
    k1 = 1
    k2 = 1

    while len(marked) < n:
        k1 += k2 - 2*k1
        k2 += k1 - 1
        marked.append(abs(k1))

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A000071 = A000071(n)

print("Sequence A000071 a(n) = Fibonacci(n) - 1:")
print(seq_A000071)
