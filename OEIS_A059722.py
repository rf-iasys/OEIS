"""
OEIS_A059722.py

Checks against OEIS A059722 online sequence if available.
Reports initial offset and any differences at the end.

Flags:
- stop_at_n_end: stop computing once x reaches n_end
- stop_at_index: stop printing once index reaches n_index_max
- use_y_values: if True, report max_y(x) values; if False, report x values
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


def compute_max_y(n_start: int, n_end: int,
                  stop_at_n_end: bool = True) -> dict[int,int]:
    max_y_per_x = {}
    n_isqrt = math.isqrt(n_end)
    for a in range(n_end // 2):
        for b in range(a + 1, a + 1 + n_isqrt):
            x = abs(a*b - b**2)
            y = x * (a*a + b**2)

            if y == 0 or x < n_start:
                continue

            if stop_at_n_end and x >= n_end:
                continue

            if y > max_y_per_x.get(x, 0):
                max_y_per_x[x] = y
    return max_y_per_x


def run(n_start: int, n_end: int, oeis_data: dict[int,int] | None = None,
        stop_at_n_end: bool = True, stop_at_index: int | None = None,
        use_y_values: bool = False) -> None:

    max_y_per_x = compute_max_y(n_start, n_end, stop_at_n_end=stop_at_n_end)

    print("\n=== OEIS A059722 ===")
    print("a(n) = n*(2*n^2 - 2*n + 1)\n")
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

        # Increment printed index only for values we will report
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
                    initial_offset = idx - 1
            else:
                print(f"[{idx:6d}] {value_to_report:12d} (Not in OEIS)")
                if first_oeis_found:
                    differences.append(value_to_report)
        else:
            print(f"[{idx:6d}] {value_to_report:12d}")

    # --- Final report ---
    print("\n=== Summary ===")
    if oeis_data is not None:
        if initial_offset > 0:
            print(f"Initial offset before first OEIS match: {initial_offset} value(s)")
        else:
            print("No initial offset; first computed value is in OEIS")
        if differences:
            print(f"Differences found (computed values not in OEIS after alignment): {differences}")
        else:
            print("No differences found; all computed values match OEIS sequence after initial offset")
    else:
        print("OEIS comparison skipped (offline or unreachable)")


def main():
    n_start = 100
    n_end = n_start + 1000
    # Flags
    stop_at_n_end = True
    stop_at_index = (n_end - 2 * n_start) // 2  # stop by index
    use_y_values = True

    oeis_url = "https://oeis.org/A059722/b059722.txt"
    try:
        oeis_data = load_oeis_data(oeis_url)
    except RuntimeError as e:
        print(f"⚠️  {e}")
        print("Proceeding without OEIS comparison.\n")
        oeis_data = None

    run(n_start, n_end, oeis_data, stop_at_n_end=stop_at_n_end,
        stop_at_index=stop_at_index, use_y_values=use_y_values)


if __name__ == "__main__":
    main()
