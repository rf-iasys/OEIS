# --------------------------
# Generate Sequence A293066
# --------------------------
def A293066(n):
    """
    Returns the first n terms of A293066,
    number of vertices at level n of PP_(4,5)
    using the cumulative sum of the deltas.
    """
    seq_a = []
    current = 1
    k = 2

    # Generate deltas
    for _ in range(n):
        seq_a.append(current)
        k += current - 2
        current += k

    # Compute cumulative sum to get A293066
    seq = []
    total = 0
    for val in seq_a:
        total += val
        seq.append(total)

    return seq

# --------------------------
# Compute coefficients of Sn(z)*(1-z)/(1+z)
# --------------------------
def transform_coefficients(seq):
    """
    Given a sequence seq[0], seq[1], ... returns
    b_n = coefficient of z^n in seq * (1-z)/(1+z)
    """
    n_terms = len(seq)
    transformed = []
    for n in range(n_terms):
        val = 0
        for k in range(n+1):
            sign = (-1)**k
            multiplier = 2 if k > 0 else 1
            val += seq[n - k] * sign * multiplier
        transformed.append(val)
    return transformed

# --------------------------
# Example usage
# --------------------------
n_terms = 100
seq_A293066 = A293066(n_terms)
seq_A107387 = transform_coefficients(seq_A293066)

print("Sequence A293066:")
print(seq_A293066)

print("\nSequence A107387 - form A(1) term:")
print(seq_A107387)
