import math

# --------------------------
# A180034
# --------------------------
def A180034(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += k + current + 1
        current += 3*k
        marked.append(k)

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A180034 = [1] + A180034(n)

print("Sequence A180034:")
print(seq_A180034)
