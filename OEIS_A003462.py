import math

# --------------------------
# Your sieve
# --------------------------
def sieve_simulation(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(current)
        k += math.floor(current/k)**2 + current + k//2
        current += k

    return marked

# --------------------------
# Example usage
# --------------------------
seq = sieve_simulation(2000)

print("Sieve sequence:")
print(seq)

# Save sequence with indices to a text file
with open("OEIS_A003462.txt", "w") as f:
    f.write("n\tsequence\n")  # Header
    for idx, number in enumerate(seq, start=1):
        f.write(f"{idx}\t{number}\n")

print("Sequence with indices saved to 'OEIS_A003462.txt'.")
