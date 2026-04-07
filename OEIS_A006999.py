import math

# --------------------------
# A006999
# --------------------------
def A006999(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append(k-1)
        k += current//2 + 1
        current += current//2 + 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 1000

# Generate A006999 sequence.
seq_A006999 = [0] + A006999(n)

print("Sequence A006999:")
print(seq_A006999)
