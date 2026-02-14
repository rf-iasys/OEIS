"""
OEIS_A258388.py

Checks against OEIS A258388 online sequence if available.
Reports initial offset, differences, and missing successors at the end.

Flags:
- stop_at_n_end: stop computing once x reaches n_end
- stop_at_index: stop printing once index reaches n_index_max
- use_y_values: if True, report max_y(x) values; if False, report x values
- primes_only: if True, only report prime values
- exclude_even: if True, skip even values
"""

import math
from sympy import primerange, isprime
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

def pi(x):
    """
    Return the number of primes <= x.
    This is the prime-counting function π(x).
    """
    primes = list(primerange(1, x+1))  # all primes <= x
    return len(primes)

def compute_max_y(n_start: int, n_end: int,
                  stop_at_n_end: bool = True) -> dict[int, int]:
    """
    Compute max_y(x) using the combinatorial formula.
    stop_at_n_end=True will skip x >= n_end
    stop_at_n_end=False will continue computing past n_end.
    Returns dict mapping x -> max_y(x).
    """
    max_y_per_x = {}
    for a in range(0, n_end):
        for b in range(a + 1, n_end):

            x = abs(a**(a+1) + b**(b+1))
            y = x * abs(a - b)

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

    print("\n=== OEIS A258388 ===")
    print("a(n) = n^(n+1) + (n-1)^n.\n")
    print(f"Numbers from {n_start} to {n_end} ({'max_y(x)' if use_y_values else 'x'}):\n")
    print(f"{'Index':>7}|{'Element':>12}| OEIS\n")

    idx = 0
    initial_offset = 0
    differences = []
    first_oeis_found = False
    reported_values = set()  # Track values we actually printed

    for x in sorted(max_y_per_x.keys()):
        if x == 1:
            continue

        y = max_y_per_x[x]

        # Fixed-point verification
        if y != x:
            continue
        
        value_to_report = y if use_y_values else x

        # ✅ Updated prime check
        if primes_only and not isprime(value_to_report):
            continue

        # Skip even numbers if exclude_even is True
        if exclude_even and value_to_report % 2 == 0:
            continue

        idx += 1

        # Stop if index exceeds stop_at_index
        if stop_at_index is not None and stop_at_index > 0 and idx > stop_at_index:
            print(f"\nStopped at index {stop_at_index}.")
            break

        reported_values.add(value_to_report)

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

    # --- Check for missing successors in OEIS ---
    missing_oeis_values = []
    if oeis_data is not None and first_oeis_found:
        # Build mapping from OEIS index -> value
        oeis_index_to_value = {idx: val for val, idx in oeis_data.items()}

        # Only consider reported values that actually exist in OEIS
        reported_oeis_indices = sorted(
            oeis_data[val] for val in reported_values if val in oeis_data
        )

        for idx in reported_oeis_indices:
            next_idx = idx + 1
            next_value = oeis_index_to_value.get(next_idx)
            if next_value is not None and next_value not in reported_values:
                missing_oeis_values.append((next_idx, next_value))

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
        if missing_oeis_values:
            print("\nOEIS values missing as successors of reported elements:")
            for oeis_idx, val in missing_oeis_values:
                print(f"  a({oeis_idx}) = {val}")
    else:
        print("OEIS comparison skipped (offline or unreachable)")

def main():
    n_start = 0
    n_end = n_start + 350
    
    # Flags
    stop_at_n_end = False
    stop_at_index = n_end
    use_y_values = False
    primes_only = False
    exclude_even = False

    oeis_url = "https://oeis.org/A258388/b258388.txt"
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
