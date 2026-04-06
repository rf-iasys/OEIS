import math

# --------------------------
# A151821
# --------------------------
def A151821(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += (k+1)*current//k
        current += current + 1
        marked.append(k+1)

    return [1] + marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A151821 = A151821(n-1)

print("Sequence A151821:")
print(seq_A151821)
