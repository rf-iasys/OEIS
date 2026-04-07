import math

# --------------------------
# A164298_Helper
# --------------------------
def A164298_Helper(n):
    marked = []
    current = 1
    k = 5

    while len(marked) < n:
        marked.append(k-1)
        k += k + current - 1
        current += k - 1

    return marked

# --------------------------
# A164298 from helper
# a(n) = ((1+4*sqrt(2))*(2+sqrt(2))^n + (1-4*sqrt(2))*(2-sqrt(2))^n)/2
#
# Formulas:
# E.g.f.: (cosh(sqrt(2)*x) + 4*sqrt(2)*sinh(sqrt(2)*x))*exp(2*x)
# --------------------------

def A164298(n):
    helper_seq = A164298_Helper(n + 1)
    seq = []
    
    for i in range(n):
        value = 2 * abs(helper_seq[i+1] - helper_seq[i])
        seq.append(value)
    
    return [1] + seq

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A164298 = A164298(n)

print("Sequence A164298:")
print(seq_A164298)
