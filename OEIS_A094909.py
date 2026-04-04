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
        k += math.floor(current / (k + 2))
        current += k

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
seq = sieve_simulation(50)
transformed_seq = transform_coefficients(seq)

print("Sieve sequence:")
print(seq)

print("\nCoefficients of Sn(z)*(1-z)/(1+z):")
print(transformed_seq)
