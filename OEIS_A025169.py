import math

# --------------------------
# Your sieve
# --------------------------
def sieve_simulation(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append(current+1)
        k += math.floor((current+2) / k)**2 + current
        current += k

    return marked

# --------------------------
# First differences
# a(n+1) - a(n)
# --------------------------
def first_differences(seq):
    return [1*(seq[i+1] - seq[i]) for i in range(len(seq)-1)]

# --------------------------
# Example usage
# --------------------------
seq = sieve_simulation(100)
diffs = first_differences(seq)

print("Sieve sequence:")
print(seq)

print("\nFirst differences a(n+1) - a(n):")
print(diffs)
