"""
OEIS_A066436_experiment.py

Experimental generator inspired by the quadratic-difference search.

x = |a^2 - b^2 - k*a*b|
y = x * (b-a)

For each x we compute max_y(x).
If max_y(x) = x we keep the value.

We use sympy.isprime to verify the results.
"""

import sympy

k = 2  # parameter in your quadratic formula

def compute_max_y(n_end):
    max_y = {}

    for a in range(n_end // 2):
        for b in range(a + 1, n_end - a + 1):
            x = abs(a**2 - b**2 - k*a*b)
            if x <= 1:
                continue  # skip 0 and 1

            y = x * (b - a)
            if y > max_y.get(x, 0):
                max_y[x] = y

    return max_y


def run(n_end=100):
    max_y = compute_max_y(n_end)

    print("\nIndex | Value | Prime?\n")
    idx = 0

    for x in sorted(max_y):
        if max_y[x] != x:
            continue

        idx += 1
        is_prime = sympy.isprime(x)
        print(f"{idx:5d} | {x:5d} | {is_prime}")


def main():
    run(1000)


if __name__ == "__main__":
    main()
