import math

# --------------------------
# A153894
# k2>1 : Expansion of (1 - x + k2*x^2)/((1-x)*(1-2*x)).
# k2=1 : a(n) = (k1+1)*2^n - 1
# --------------------------
def A153894(n):
    marked = []
    current = 1
    k1 = 4
    k2 = 1
    k = k1
    
    while len(marked) < n:
        marked.append(k)
        k += k + k2
        current += k//2

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A153894 = A153894(n+1)

print("Sequence A153894:")
print(seq_A153894)
