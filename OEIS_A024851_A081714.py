import math

# --------------------------
# A024851 sieve
# --------------------------
def sieve_A024851(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append(current)
        k += math.floor(current/k) + current - 2
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
# Extract first 1000 terms
# --------------------------
n_terms = 20

seq_A024851 = sieve_A024851(n_terms)
seq_A081714 = transform_coefficients(seq_A024851)

print("Sequence A024851:")
print(seq_A024851)

print("\nSequence A081714 from term A(1):")
print(seq_A081714)
