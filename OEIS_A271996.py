import math

# --------------------------
# Your sieve
# --------------------------
def sieve_simulation(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append(current)
        k += math.floor((2*current) / k)**2
        current += k

    return marked

# --------------------------
# First differences
# a(n+1) - a(n)
# --------------------------
def first_differences_doubled(seq):
    return [2*(seq[i+1] - seq[i]) for i in range(len(seq)-1)]

# --------------------------
# Example usage
# --------------------------
seq = sieve_simulation(50)
diffs = first_differences_doubled(seq)

print("Sieve sequence:")
print(seq)

print("\nFirst differences a(n+1) - a(n):")
print(diffs)
