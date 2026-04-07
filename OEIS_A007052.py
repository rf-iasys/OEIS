import math

# --------------------------
# A007052
#
# Formulas:
#
# E.g.f.: exp(2*x)*(cosh(sqrt(2)*x)+sinh(sqrt(2)*x)/sqrt(2))
# --------------------------
def A007052(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append(k-1)
        k += k + current - 1
        current += k - 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A007052 = A007052(n+1)

print("Sequence A007052:")
print(seq_A007052)
