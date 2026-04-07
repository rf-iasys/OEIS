import math

# --------------------------
# A161941
# a(n) = ((4+sqrt(2))*(2+sqrt(2))^n + (4-sqrt(2))*(2-sqrt(2))^n)/4
#
# Formulas:
# a(n) = 2*A007070(n) - 3*A007070(n-1)
# --------------------------
def A161941(n):
    marked = []
    current = 1
    k = 3

    while len(marked) < n:
        marked.append(k-1)
        k += k + current - 1
        current += k - 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A161941 = A161941(n+1)

print("Sequence A161941:")
print(seq_A161941)
