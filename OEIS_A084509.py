from fractions import Fraction
from math import lcm

# --------------------------
# Helper sequence
# --------------------------
def A084509_Helper(n):
    """
    Helper sequence for generating A084509.
    """
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(k)
        k += k * current // k
        current += current + 3 * k

    return marked

# --------------------------
# Compute inverse generating function (absolute values)
# --------------------------
def inverse_series_abs(a, n_terms):
    """
    Computes the coefficients of 1/S(z), where S(z) has coefficients `a`.
    Takes absolute values to produce positive integers.
    """
    b = [Fraction(0) for _ in range(n_terms)]
    b[0] = Fraction(1, a[0])

    for n in range(1, n_terms):
        s = Fraction(0)
        for k in range(1, n+1):
            s += a[k] * b[n-k]
        b[n] = -s / a[0]

    return [abs(x) for x in b]

# --------------------------
# Convert fractions to integers
# --------------------------
def to_integers(frac_seq):
    """
    Converts a list of Fractions to integers by multiplying by LCM of denominators.
    """
    denominators = [x.denominator for x in frac_seq]
    common_lcm = 1
    for d in denominators:
        common_lcm = lcm(common_lcm, d)

    return [int(x * common_lcm) for x in frac_seq]

# --------------------------
# Generate A084509 using A084509_Helper
# --------------------------
def generate_A084509(n_terms):
    """
    Generates the first n_terms of A084509 using A084509_Helper.
    """
    helper_seq = A084509_Helper(n_terms)
    inverse_frac = inverse_series_abs(helper_seq, n_terms)
    A084509_seq = [1] + to_integers(inverse_frac)
    return helper_seq, A084509_seq

# --------------------------
# Main execution
# --------------------------
if __name__ == "__main__":
    n_terms = 1662  # OEIS has terms 0..1662

    helper_seq, A084509_seq = generate_A084509(n_terms)

    print("\nDerived sequence A084509 (first 20 terms):")
    print(A084509_seq[:20])

    # Save A084509 to file
    filename = "OEIS_A084509.txt"
    with open(filename, "w") as f:
        f.write(', '.join(str(x) for x in A084509_seq))

    print(f"\nA084509 sequence saved to '{filename}'")
