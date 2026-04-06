import math

# --------------------------
# A095121 - Expansion of (1 - x + k2*x^2)/((1-x)*(1-2*x)).
# --------------------------
def A095121(n):
    marked = []
    current = 1
    k1 = 2
    k2 = 2
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

seq_A095121 = [1] + A095121(n)

print("Sequence A095121:")
print(seq_A095121)
