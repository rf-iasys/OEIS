import math

# --------------------------
# A000295
# --------------------------
def A000295(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + current + 1
        current += 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 500

seq_A000295 = [0,0] + A000295(n-1)

print("Sequence A000295:")
print(seq_A000295)
