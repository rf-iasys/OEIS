import math

# --------------------------
# A003945
# --------------------------
def A003945(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + current//k
        current += current - 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A003945 = A003945(n+1)

print("Sequence A003945:")
print(seq_A003945)
