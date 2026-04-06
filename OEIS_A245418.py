import math

# --------------------------
# A245418_Helper
# --------------------------
def A245418_Helper(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k - k//3
        current += k + 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 200

seq_A245418_Helper = A245418_Helper(n)

# --------------------------
# Create sequence A245418
# --------------------------
A245418 = [5] + [5 * abs(seq_A245418_Helper[i+1] - seq_A245418_Helper[i]) for i in range(len(seq_A245418_Helper)-1)]

print("\nSequence A245418:")
print(A245418)
