import math

# --------------------------
# A083329
# --------------------------
def A083329(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + current//(2*k)
        current += k + 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 1000

seq_A083329 = A083329(n+1)

print("Sequence A083329:")
print(seq_A083329)
