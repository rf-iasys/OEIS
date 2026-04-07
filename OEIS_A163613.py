import math

# --------------------------
# A163613_Helper
# --------------------------
def A163613_Helper(n):
    marked = []
    current = 1
    k = 4

    while len(marked) < n:
        marked.append(k-1)
        k += k + current - 1
        current += k - 1

    return marked

# --------------------------
# A163613 from helper
# a(n) = ((1 + 3*sqrt(2))*(2 + sqrt(2))^n + (1 - 3*sqrt(2))*(2 - sqrt(2))^n)/2
#
# Formulas:
# E.g.f.: exp(2*x)*( cosh(sqrt(2)*x) + 3*sqrt(2)*sinh(sqrt(2)*x))
# --------------------------

def A163613(n):
    helper_seq = A163613_Helper(n + 1)
    seq = []
    
    for i in range(n):
        value = 2 * abs(helper_seq[i+1] - helper_seq[i])
        seq.append(value)
    
    return [1] + seq

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A163613 = A163613(n)

print("Sequence A163613:")
print(seq_A163613)
