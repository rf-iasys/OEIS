"""
Compare combinatorial max_y results with OEIS A069131 sequence.
"""

import math
import requests

def load_oeis_data(url: str) -> dict[int, int]:
    """Load OEIS b-file data from URL as value -> index dict."""
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    oeis_data = {}
    for line in response.text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            idx, value = line.split()
            idx = int(idx)
            value = int(value)
            if value not in oeis_data:
                oeis_data[value] = idx
        except ValueError:
            continue
    return oeis_data

def compute_max_y(n_start: int, n_end: int,
                  stop_at_n_end: bool = True) -> dict[int, int]:
    """
    Compute max_y(x) using the combinatorial formula.
    """
    max_y_per_x = {}
    n_isqrt = math.isqrt(n_end)

    for a in range(n_isqrt):
        for b in range(a + 1, 2 * a):
            x = round((a**0.5 * b**0.5 + a + b) ** 2)
            y = x * abs(a - b)

            if y == 0 or x < n_start:
                continue

            if stop_at_n_end and x >= n_end:
                continue

            if y > max_y_per_x.get(x, 0):
                max_y_per_x[x] = y

    return max_y_per_x

def run_comparison(n_start: int, n_end: int, oeis_data: dict[int, int] | None = None):
    max_y_per_x = compute_max_y(n_start, n_end)

    print("\n=== OEIS A069131 ===")
    print("Centered 18-gonal numbers.\n")
    print(f"Numbers from {n_start} to {n_end} (x):\n")
    print(f"{'Index':>7}|{'Element':>7}| OEIS\n")

    sorted_x = sorted(max_y_per_x.keys())
    idx = 0
    initial_offset = 0
    differences = []
    first_oeis_found = False

    for x in sorted_x:
        if x == 1:
            continue

        y = max_y_per_x[x]

        # Fixed-point verification
        if y != x:
            continue

        idx += 1
        value_to_report = x

        if oeis_data is not None:
            if value_to_report in oeis_data:
                oeis_index = oeis_data[value_to_report]
                print(f"[{idx:6d}] {value_to_report:6d} (OEIS: a({oeis_index}) = {value_to_report})")
                if not first_oeis_found:
                    first_oeis_found = True
                    initial_offset = idx - 1
            else:
                print(f"[{idx:6d}] {value_to_report:6d} (Not in OEIS)")
                if first_oeis_found:
                    differences.append(value_to_report)
        else:
            print(f"[{idx:6d}] {value_to_report:6d}")

    # --- OEIS Summary ---
    print("\n=== OEIS Summary ===")
    if oeis_data is not None:
        if initial_offset > 0:
            print(f"Initial offset before first OEIS match: {initial_offset} value(s)")
        else:
            print("No initial offset; first computed value is in OEIS")

        if differences:
            print(f"Differences found: {differences}")
        else:
            print("No differences found; all computed values match OEIS sequence")
    else:
        print("OEIS comparison skipped (offline or unreachable)")

def main():
    n_start = 0
    n_end = 10000
    oeis_url = "https://oeis.org/A069131/b069131.txt"

    try:
        oeis_data = load_oeis_data(oeis_url)
    except Exception as e:
        print(f"⚠️ Failed to load OEIS data: {e}")
        oeis_data = None

    run_comparison(n_start, n_end, oeis_data)

if __name__ == "__main__":
    main()
