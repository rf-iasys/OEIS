# --------------------------
# Generate A112088
# --------------------------
def A112088(n):
    prev = 1
    current = 1
    diff_seq = []

    for _ in range(n):
        k = prev + prev//2 + 2*current
        diff_seq.append(k - prev)
        current += current//k
        prev = k

    return diff_seq

# --------------------------
# Compute first n terms of A112088
# --------------------------
n = 5678
seq_A112088 = A112088(n)

# --------------------------
# Save sequence to a txt file
# --------------------------
filename = "OEIS_A112088.txt"

with open(filename, "w") as f:
    # Write as comma-separated values
    f.write(', '.join(str(x) for x in seq_A112088))

print(f"Sequence A112088 saved to '{filename}'")
