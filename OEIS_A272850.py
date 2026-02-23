"""
OEIS_A272850.py

Checks against OEIS A272850 online sequence if available.
Reports initial offset and any differences at the end.

Flags:
- stop_at_n_end: stop computing once x reaches n_end
- use_y_values: if True, report max_y(x) values; if False, report x values
"""

import math
import requests

def load_oeis_data(url: str) -> dict[int,int]:
    """
    Loads OEIS b-file data from a URL.
    Returns a dict mapping OEIS value -> index in the sequence.
    Raises RuntimeError if fetch fails.
    """
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
    """
    Compute max_y(x) using the combinatorial formula.
    stop_at_n_end=True will skip x >= n_end
    stop_at_n_end=False will continue computing past n_end.
    Returns dict mapping x -> max_y(x).
    """
    max_y_per_x = {}
    n_isqrt = math.isqrt(n_end)
    for a in range(n_end // 2):
        for b in range(a + 1, a + 1 + n_isqrt):
            x = abs(a**4 - b**4)*abs(a**2-b**2)
            y = x * abs(b - a)

            if y == 0 or x < n_start:
                continue

            if stop_at_n_end and x >= n_end:
                continue

            if y > max_y_per_x.get(x, 0):
                max_y_per_x[x] = y
    return max_y_per_x


def run(n_start: int, n_end: int, oeis_data: dict[int,int] | None = None,
        stop_at_n_end: bool = True, use_y_values: bool = False) -> None:

    max_y_per_x = compute_max_y(n_start, n_end, stop_at_n_end=stop_at_n_end)

    print("\n=== OEIS A272850 ===")
    print("a(n) = (n^2 + (n+1)^2)*(n^2 + (n+1)^2 + 2*n*(n+1)).\n")
    print(f"Numbers from {n_start} to {n_end} ({'max_y(x)' if use_y_values else 'x'}):\n")
    print(f"{'Index':>7}|{'Element':>7}| OEIS\n")

    idx = 0
    initial_offset = 0
    differences = []
    first_oeis_found = False

    for x in sorted(max_y_per_x.keys()):
        if x == 1:
            continue

        y = max_y_per_x[x]

        # 🔒 Fixed-point verification: x == max_y(x)
        if y != x:
            continue

        idx += 1
        value_to_report = y if use_y_values else x

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
    n_start = 0
    n_end = n_start + 100000
    # Flags
    stop_at_n_end = True    # Continue computing beyond n_end if False
    use_y_values = False    # Report x (False) or max_y(x) (True)

    oeis_url = "https://oeis.org/A272850/b272850.txt"
    try:
        oeis_data = load_oeis_data(oeis_url)
    except RuntimeError as e:
        print(f"⚠️  {e}")
        print("Proceeding without OEIS comparison.\n")
        oeis_data = None

    run(n_start, n_end, oeis_data, stop_at_n_end=stop_at_n_end, use_y_values=use_y_values)


if __name__ == "__main__":
    main()
