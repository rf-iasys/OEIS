import math

# --------------------------
# A081704
# --------------------------
def A081704(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += 2*k + current//2
        current += 2*k

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A081704 = A081704(n+1)

print("Sequence A081704:")
print(seq_A081704)
