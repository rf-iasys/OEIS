import math

# --------------------------
# A245430_Helper
# --------------------------
def A245430_Helper(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k - k//5
        current += k + 1

    return marked

# --------------------------
# Calculate 1st n terms
# --------------------------
n = 100

seq_A245430_Helper = A245430_Helper(n)

# --------------------------
# Create sequence A245430
# --------------------------
A245430 = [9] + [9 * abs(seq_A245430_Helper[i+1] - seq_A245430_Helper[i]) for i in range(len(seq_A245430_Helper)-1)]

print("\nSequence A245430:")
print(A245430)
