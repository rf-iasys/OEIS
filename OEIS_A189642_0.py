"""
OEIS_A189642.py

Computes sequence and checks against OEIS A189642 (online if available).
Annotates results with prime factors and multiples of OEIS (3x, 9x).

Flags:
- stop_at_n_end: stop computing once x reaches n_end
- stop_at_index: stop printing once index reaches n_index_max
- use_y_values: if True, report max_y(x) values; if False, report x values
- primes_only: if True, only report prime values
- exclude_even: if True, skip even values
"""

import math
from sympy import primerange, factorint
import requests

def load_oeis_data(url: str) -> dict[int,int]:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except Exception:
        raise RuntimeError("Failed to fetch OEIS data (offline or URL unreachable)")

    lines = response.text.splitlines()
    oeis_data = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            index, value = line.split()
            index = int(index)
            value = int(value)
            if value not in oeis_data:
                oeis_data[value] = index
        except ValueError:
            continue
    return oeis_data

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def pi(x):
    """Return number of primes <= x."""
    primes = list(primerange(1, x+1))
    return len(primes)

def compute_max_y(n_start: int, n_end: int,
                  stop_at_n_end: bool = True) -> dict[int, int]:
    max_y_per_x = {}
    
    for a in range(2, n_end):
        b = a + 1
        x = abs(a**2 - b**2 + a*b*(a+b))

        if stop_at_n_end and x >= n_end:
            continue

        if x > max_y_per_x.get(x, 0):
            max_y_per_x[x] = x

    return max_y_per_x

def run(n_start: int, n_end: int, oeis_data: dict[int,int] | None = None,
        stop_at_n_end: bool = True, stop_at_index: int | None = None,
        use_y_values: bool = False, primes_only: bool = False,
        exclude_even: bool = False) -> None:

    max_y_per_x = compute_max_y(n_start, n_end, stop_at_n_end=stop_at_n_end)

    print("\n=== OEIS A189642 ===")
    print("Numerator of H(n+4) - H(n), where H(n) = Sum_{k=1..n} 1/k.\n")
    print(f"{'Index':>7}|{'Element':>12}| OEIS | Factors\n")

    idx = 0
    initial_offset = 0
    differences = []
    first_oeis_found = False

    for x in max_y_per_x.keys():  # preserve original order
        if x == 1:
            continue

        y = max_y_per_x[x]

        # Fixed-point verification
        if y != x:
            continue

        value_to_report = y if use_y_values else x

        # Skip non-primes if needed
        if primes_only and not is_prime(value_to_report):
            continue

        # Skip even numbers if needed
        if exclude_even and value_to_report % 2 == 0:
            continue

        idx += 1
        if stop_at_index is not None and stop_at_index > 0 and idx > stop_at_index:
            print(f"\nStopped at index {stop_at_index}.")
            break

        # Prime factorization
        factors = factorint(value_to_report)
        factors_str = " * ".join(
            [f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(factors.items())]
        )

        # OEIS detection
        tag = "Not in OEIS"
        if oeis_data is not None:
            if value_to_report in oeis_data:
                oeis_index = oeis_data[value_to_report]
                tag = f"OEIS: a({oeis_index}) = {value_to_report}"
            elif value_to_report % 3 == 0 and (value_to_report // 3) in oeis_data:
                oeis_index = oeis_data[value_to_report // 3]
                tag = f"3×OEIS: a({oeis_index}) = {value_to_report//3}"
            elif value_to_report % 9 == 0 and (value_to_report // 9) in oeis_data:
                oeis_index = oeis_data[value_to_report // 9]
                tag = f"9×OEIS: a({oeis_index}) = {value_to_report//9}"

        print(f"[{idx:6d}] {value_to_report:12d} ({tag}) | {factors_str}")

    print("\n=== Summary ===")
    if oeis_data is not None:
        if first_oeis_found:
            if initial_offset != 0:
                print(f"Initial offset before first OEIS match: {initial_offset} value(s)")
            else:
                print("No initial offset; first computed value is in OEIS")
        else:
            print("No matches found in OEIS data")
    else:
        print("OEIS comparison skipped (offline or unreachable)")

def main():
    n_start = 0
    n_end = n_start + 1000

    # Flags
    stop_at_n_end = False
    stop_at_index = 0
    use_y_values = False
    primes_only = False
    exclude_even = False

    oeis_url = "https://oeis.org/A189642/b189642.txt"
    try:
        oeis_data = load_oeis_data(oeis_url)
    except RuntimeError as e:
        print(f"⚠️  {e}")
        print("Proceeding without OEIS comparison.\n")
        oeis_data = None

    run(n_start, n_end, oeis_data, stop_at_n_end=stop_at_n_end,
        stop_at_index=stop_at_index, use_y_values=use_y_values,
        primes_only=primes_only, exclude_even=exclude_even)

if __name__ == "__main__":
    main()
