import math

# --------------------------
# A127968 - a(n) = F(n+1) + (1-(-1)^n)/2, where F() = Fibonacci numbers A000045
# --------------------------
def A127968(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += current - 1
        current += k
        marked.append(k)
        marked.append(current)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A127968 = A127968(n+1)

print("Sequence A127968:")
print(seq_A127968[:n+1])
