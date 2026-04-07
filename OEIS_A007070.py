import math

# --------------------------
# A007070
# a(n) = (2 - sqrt(2))^n*(1/2 - sqrt(2)/2) + (2 + sqrt(2))^n*(1/2 + sqrt(2)/2)
#
# Formulas:
# 
# E.g.f.: exp(2*x)*(cosh(sqrt(2)*x) + sqrt(2)*sinh(sqrt(2)*x))
# --------------------------
def A007070(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += k + current - 1
        current += k - 1
        marked.append(k-1)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A007070 = A007070(n+1)

print("Sequence A007070:")
print(seq_A007070)
