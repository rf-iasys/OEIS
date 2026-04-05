import math

# --------------------------
# A033638
# --------------------------
def A033638(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(current)
        k += 1
        current += k//2

    return marked

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
        # convolution with 1, -2, 2, -2, ... (from (1-z)/(1+z))
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
n = 100

seq_A033638 = A033638(n)
seq_A057979 = transform_coefficients(seq_A033638)

print("Sequence A033638:")
print(seq_A033638)

print("\nSequence A057979:")
print(seq_A057979)
