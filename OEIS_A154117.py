import math

# --------------------------
# A154117 - a(n) = (k1+k2)*2^(n-1) - k2
# --------------------------
def A154117(n):
    marked = []
    current = 1
    k1 = 2
    k2 = 3
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

seq_A154117 = [1] + A154117(n)

print("Sequence A154117:")
print(seq_A154117)
