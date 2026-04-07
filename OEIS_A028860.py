import math

# --------------------------
# A028860
# --------------------------
def A028860(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += current - 2*k
        current += current + k

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 1000

# Generate A028860 sequence.
seq_A028860 = [-1] + A028860(n)

print("Sequence A028860:")
print(seq_A028860)
