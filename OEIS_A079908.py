"""
OEIS_A079908.py

Checks against OEIS A079908 online sequence if available.
Reports initial offset and any differences at the end.

Flags:
- stop_at_n_end: stop computing once x reaches n_end
- stop_at_index: stop printing once index reaches n_index_max
- use_y_values: if True, report max_y(x) values; if False, report x values
- primes_only: if True, only report prime values
- exclude_even: if True, skip even values
"""

import math
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
    "Simple primality test for positive integers."
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

def compute_max_y(n_start: int, n_end: int,
                  stop_at_n_end: bool = True) -> dict[int,int]:
    """
    Compute max_y(x) using the combinatorial formula.
    stop_at_n_end=True will skip x >= n_end
    Returns dict mapping x -> max_y(x).
    """
    max_y_per_x = {}

    for a in range(1, n_end//2):
        for b in range(a + 1, n_end - a):

            x = a*b
            y = x * abs(3*a + x*b)

            if y == 0 or x < n_start:
                continue

            if stop_at_n_end and x >= n_end:
                continue

            if y > max_y_per_x.get(x, 0):
                max_y_per_x[x] = y
    return max_y_per_x

def run(n_start: int, n_end: int, oeis_data: dict[int,int] | None = None,
        stop_at_n_end: bool = True, stop_at_index: int | None = None,
        use_y_values: bool = False, primes_only: bool = False,
        exclude_even: bool = False) -> None:

    max_y_per_x = compute_max_y(n_start, n_end, stop_at_n_end=stop_at_n_end)

    print("\n=== OEIS A079908 ===")
    print("Solution to the Dancing School Problem with 3 girls and n+3 boys: f(3,n)\n")
    print(f"Numbers from {n_start} to {n_end} ({'max_y(x)' if use_y_values else 'x'}):\n")
    print(f"{'Index':>7}|{'Element':>12}| OEIS\n")

    idx = 0
    initial_offset = 0
    differences = []
    first_oeis_found = False

    for x in sorted(max_y_per_x.keys()):
        if x == 1:
            continue

        y = max_y_per_x[x]
        value_to_report = y if use_y_values else x

        # 🔒 Skip non-primes if primes_only is True
        if primes_only and not is_prime(value_to_report):
            continue

        # 🔒 Skip even numbers if exclude_even is True
        if exclude_even and value_to_report % 2 == 0:
            continue

        # Increment printed index only for reported values
        idx += 1

        # Stop completely if index exceeds stop_at_index
        if stop_at_index is not None and stop_at_index > 0 and idx > stop_at_index:
            print(f"\nStopped at index {stop_at_index}.")
            break

        if oeis_data is not None:
            if value_to_report in oeis_data:
                oeis_index = oeis_data[value_to_report]
                print(f"[{idx:6d}] {value_to_report:12d} (OEIS: a({oeis_index}) = {value_to_report})")
                if not first_oeis_found:
                    first_oeis_found = True
                    initial_offset = oeis_index - idx
            else:
                print(f"[{idx:6d}] {value_to_report:12d} (Not in OEIS)")
                if first_oeis_found:
                    differences.append(value_to_report)
        else:
            print(f"[{idx:6d}] {value_to_report:12d}")

    # --- Final report ---
    print("\n=== Summary ===")
    if oeis_data is not None:
        if first_oeis_found:
            if initial_offset != 0:
                print(f"Initial offset before first OEIS match: {initial_offset} value(s)")
            else:
                print("No initial offset; first computed value is in OEIS")
        else:
            print("No matches found in OEIS data")
        if differences:
            print(f"Differences found (computed values not in OEIS after alignment): {differences}")
        else:
            print("No differences found; all computed values match OEIS sequence after initial offset")
    else:
        print("OEIS comparison skipped (offline or unreachable)")

def main():
    n_start = 0
    n_end = n_start + 1000
    # Flags
    stop_at_n_end = True
    stop_at_index = n_end - 4
    use_y_values = True
    primes_only = False
    exclude_even = False

    oeis_url = "https://oeis.org/A079908/b079908.txt"
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
