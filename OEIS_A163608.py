import math

# --------------------------
# A163608
# a(n) = ((5 + 2*sqrt(2))*(2 + sqrt(2))^n + (5 - 2*sqrt(2))*(2 - sqrt(2))^n)/2.
#
# Formulas:
# a(n) = 5*A007070(n) - 6*A007070(n-1)
# E.g.f.: exp(2*x)*( 5*cosh(sqrt(2)*x) + 2*sqrt(2)*sinh(sqrt(2)*x))
# --------------------------

def A163608(n):
    marked = []
    current = 1
    k = -2

    while len(marked) < n:
        k += k + current - 1
        current += k - 1
        marked.append(abs(k-1))

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A163608 = A163608(n+1)

print("Sequence A163608:")
print(seq_A163608)
