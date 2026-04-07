import math

# --------------------------
# A152009
# --------------------------
def A152009(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += k//2 + current//k
        current += k + 1
        marked.append(k+1)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A152009 = A152009(n+1)

print("Sequence A152009:")
print(seq_A152009)
