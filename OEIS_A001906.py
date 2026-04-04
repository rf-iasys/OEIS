import math

# --------------------------
# Your sieve
# --------------------------
def sieve_simulation(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append((current+1)//2)
        k += math.floor((current+2)/k)**2 + current
        current += k

    return marked

# --------------------------
# Example usage
# --------------------------
seq = sieve_simulation(3000)

# Save sequence with indices to a text file
with open("OEIS_A001906.txt", "w") as f:
    f.write("n\tsequence\n")  # Header
    for idx, number in enumerate(seq, start=1):
        f.write(f"{idx}\t{number}\n")

print("Sequence with indices saved to 'OEIS_A001906.txt'.")
