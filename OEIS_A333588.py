import math

# --------------------------
# A333588 Helper
# --------------------------
def A333588_helper(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        k += current - 2*k
        current += current // 2 - k
        marked.append(k)

    return marked

# --------------------------
# Create sequence A333588
# --------------------------
def A333588(n):
    seq_A333588_helper = A333588_helper(n+2)  # need n+2 terms to compute n+1 differences
    differences = [seq_A333588_helper[i+1] - seq_A333588_helper[i] for i in range(n+1)]
    return differences[1:]  # exclude the first element

# --------------------------
# Calculate sequences
# --------------------------
n = 42

seq_A333588 = A333588(n)

print("Sequence A333588:")
print(seq_A333588)
