import math

# --------------------------
# A076883
# --------------------------
def A076883(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + k//2
        current += k + 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A076883 = A076883(n)

print("Sequence A076883:")
print(seq_A076883)
