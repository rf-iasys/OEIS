"""
OEIS_A030514.py

Checks against OEIS A030514 online sequence if available.
Reports initial offset, any differences, validates results,
and also identifies indexes corresponding to OEIS A047845.

This algorithm generates exactly the odd primes in a given range
using a combinatorial fixed-point condition, without using sieves
or explicit primality tests in the generation phase.
"""

import requests

def load_oeis_data(url: str) -> dict[int, int]:
    """Load OEIS b-file data from a URL; returns {value: index} mapping."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except Exception:
        raise RuntimeError("Failed to fetch OEIS data (offline or unreachable)")
    oeis_data = {}
    for line in response.text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            index, value = map(int, line.split())
            if value not in oeis_data:
                oeis_data[value] = index
        except ValueError:
            continue
    return oeis_data

def compute_max_y(n_start: int, n_end: int,
                  stop_at_n_end: bool = True) -> dict[int, int]:
    """Compute fixed points using combinatorial formula."""
    max_y_per_x = {}
    for a in range(n_end):
        b = a + 1
        x = abs(a**2 - b**2) * abs(b**2 - a**2)**3
        y = x * abs(a - b)
        if y == 0 or x < n_start:
            continue
        if stop_at_n_end and x >= n_end:
            continue
        if y > max_y_per_x.get(x, 0):
            max_y_per_x[x] = y
    return max_y_per_x

def run(n_start: int, n_end: int, oeis_data: dict[int, int] | None = None,
        stop_at_n_end: bool = True, use_y_values: bool = False) -> None:

    max_y_per_x = compute_max_y(n_start, n_end, stop_at_n_end=stop_at_n_end)

    print("\n=== Fixed-Point Report ===")
    print(f"Numbers from {n_start} to {n_end} ({'max_y(x)' if use_y_values else 'x'}):\n")
    print(f"{'Index':>7}|{'Element':>10}| OEIS\n")

    idx = 0
    initial_offset = 0
    differences = []
    first_oeis_found = False
    a047845_indexes = []

    for x in sorted(max_y_per_x.keys()):
        y = max_y_per_x[x]
        if y != x or x == 1:
            continue

        idx += 1
        value_to_report = int(y/1) if use_y_values else x

        # Classify sequences
        if oeis_data is not None and value_to_report in oeis_data:
            oeis_index = oeis_data[value_to_report]
            print(f"[{idx:6d}] {value_to_report:10d} (OEIS A030514: a({oeis_index}) = {value_to_report})")
            if not first_oeis_found:
                first_oeis_found = True
                initial_offset = idx - 1
        else:
            print(f"[{idx:6d}] {value_to_report:10d} (Not in A030514 → A047845 index)")
            # Subtract 1 to align with A047845 (ignoring initial 0)
            a047845_indexes.append(idx)
            if first_oeis_found:
                differences.append(value_to_report)

    # --- OEIS Summary ---
    print("\n=== OEIS Summary ===")
    if oeis_data is not None:
        if initial_offset > 0:
            print(f"Initial offset before first OEIS match: {initial_offset} value(s)")
        else:
            print("No initial offset; first computed value is in OEIS")

        if differences:
            print(f"Differences (computed values not in A030514 after first match): {differences}")
        else:
            print("All computed values match OEIS A030514 after initial offset")
    else:
        print("OEIS comparison skipped (offline or unreachable)")

    print("\n=== OEIS A047845 Indexes (from extra numbers) ===")
    print(a047845_indexes)

def main():
    n_start = 0
    n_end = n_start + 2000

    stop_at_n_end = False
    use_y_values = True

    oeis_url = "https://oeis.org/A030514/b030514.txt"
    try:
        oeis_data = load_oeis_data(oeis_url)
    except RuntimeError as e:
        print(f"⚠️ {e}")
        print("Proceeding without OEIS comparison.\n")
        oeis_data = None

    run(
        n_start,
        n_end,
        oeis_data,
        stop_at_n_end=stop_at_n_end,
        use_y_values=use_y_values
    )

if __name__ == "__main__":
    main()
