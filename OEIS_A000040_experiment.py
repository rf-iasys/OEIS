"""
OEIS_A000040_experiment.py

Experimental generator inspired by the quadratic-difference search.

x = |a^2 - b^2|
y = x(b-a)

For each x we compute max_y(x).
If max_y(x) = x we keep the value.

Empirically this yields the prime numbers.
"""

import math
import requests

k = 0

def load_oeis_data(url: str):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
    except Exception:
        return None

    data = {}
    for line in r.text.splitlines():
        if line.startswith("#") or not line.strip():
            continue
        i, v = line.split()
        data[int(v)] = int(i)
    return data


def compute_max_y(n_end):

    max_y = {}

    for a in range(n_end//2):
        for b in range(a + 1, n_end - a + 1):

            x = abs(a**2 - b**2 - k*a*b)
            y = x * (b-a)

            if x <= 0:
                continue

            if y > max_y.get(x, 0):
                max_y[x] = y

    return max_y


def run(n_end=100):

    max_y = compute_max_y(n_end)

    print("\nIndex | Value\n")

    idx = 0

    for x in sorted(max_y):

        if max_y[x] != x:
            continue

        idx += 1
        print(f"{idx:5d} | {x}")


def main():

    run(1000)


if __name__ == "__main__":
    main()
