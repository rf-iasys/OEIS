import math

# --------------------------
# A161938
# a(n) = ((3+sqrt(2))*(2+sqrt(2))^n + (3-sqrt(2))*(2-sqrt(2))^n)/2
#
# Formulas:
# --------------------------

def A161938(n):
    marked = []
    current = 1
    k = -1

    while len(marked) < n:
        k += k + current - 1
        current += k - 1
        marked.append(abs(k-1))

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A161938 = A161938(n+1)

print("Sequence A161938:")
print(seq_A161938)
