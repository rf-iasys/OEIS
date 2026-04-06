# --------------------------
# Official A112088 formula
# --------------------------
def official_A112088(n_terms):
    sequence = [2]
    running_sum = 2
    for _ in range(1, n_terms):
        next_term = (5 + running_sum) // 2
        sequence.append(next_term)
        running_sum += next_term
    return sequence

# --------------------------
# Custom implementation
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
# Comparison for large n
# --------------------------
n_terms = 10000
official_seq = official_A112088(n_terms)
custom_seq = A112088(n_terms)

differences = [(i+1, o, c) for i, (o, c) in enumerate(zip(official_seq, custom_seq)) if o != c]

if differences:
    print(f"Differences found in {len(differences)} terms. First few differences:")
    for diff in differences[:10]:  # show only first 10 differences
        print(f"Term {diff[0]}: Official={diff[1]}, Custom={diff[2]}")
else:
    print("No differences found — both sequences match for all 10,000 terms.")
