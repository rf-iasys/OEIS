import math

# --------------------------
# A006012
# --------------------------
def A006012(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append((k+1)//3)
        k += k + current
        current += k + 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A006012 = A006012(n+1)

print("Sequence A006012:")
print(seq_A006012)
