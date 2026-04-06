import math

# --------------------------
# A147722
# --------------------------
def A147722(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + current - 1
        current += 2*k

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A147722 = A147722(n+1)

print("Sequence A147722:")
print(seq_A147722)
