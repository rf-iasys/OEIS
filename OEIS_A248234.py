import math

def a248234_terms(n_max: int):
    """Generator for A248234 replacement formula, readable version."""
    for n in range(2, n_max + 2):
        base = (2*(n-1)+1)*(2*(n-1)**3 + 3*(n-1)**2 + 3*(n-1) + 1)
        if n <= 3:
            if n == 3:
                term = base + 1
            else:
                term = base
        else:
            term = base + (n-3) + math.ceil(((n-2)**2 - 1)/3)
        yield term

# Print first 2000 terms with 1-based index
for i, val in enumerate(a248234_terms(2000), start=1):
    print(f"{i}: {val}")
