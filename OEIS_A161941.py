import math

# --------------------------
# A161941
# --------------------------
def Sieve(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k + 3*current
        current += current//k + k//3

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A161941 = Sieve(n+1)

# --------------------------
# Compute A161941
# --------------------------
diff_A161941 = [2]+[(seq_A161941[i+2] - seq_A161941[i])//3 for i in range(len(seq_A161941) - 2)]

print("Sequence A161941:")
print(diff_A161941)
