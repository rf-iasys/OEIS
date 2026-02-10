"""
OEIS_A005563.py

Brute-force streaming computation of max_y(x) values using the combinatorial formula
y = x * |x - (a+b)^2|.

Checks against OEIS A005563 online sequence if available.
Reports initial offset and any differences at the end.
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
    for line in lines[1:]:
        if line.startswith("#"):
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


def compute_max_y(n_end: int) -> dict[int,int]:
    """
    Compute max_y(x) using the combinatorial formula; return as dict mapping x -> max_y(x).
    Stop computing once max_y >= n_end.
    """
    max_y_per_x = dict()
    n_isqrt = math.isqrt(n_end)
    for a in range(n_end // 2):
        for b in range(a + 1, a + 1 + n_isqrt):

            x = a*b + a
            y = x * abs(a*b - a)

            if y == 0:
                continue
            if y >= n_end:
                # stop early
                return max_y_per_x
            if 0 <= x < n_end:
                if y > max_y_per_x.get(x, 0):
                    max_y_per_x[x] = y
    return max_y_per_x


def run(n_end: int, oeis_data: dict[int,int] | None = None) -> None:
    max_y_per_x = compute_max_y(n_end)

    print("\n=== OEIS A005563 ===")
    print("a(n) = n*(n+2) = (n+1)^2 - 1\n")
    print(f"Numbers from 0 to {n_end} (max_y(x)):\n")

    idx = 0
    initial_offset = 0
    differences = []
    first_oeis_found = False

    for x in sorted(max_y_per_x.keys()):
        if x == 1:
            continue
        y = max_y_per_x[x]
        idx += 1

        if oeis_data is not None:
            if y in oeis_data:
                oeis_index = oeis_data[y]
                print(f"[{idx:6d}] {y:6d} (OEIS: a({oeis_index}) = {y})")
                if not first_oeis_found:
                    first_oeis_found = True
                    initial_offset = idx - 1  # count of leading y not in OEIS
            else:
                print(f"[{idx:6d}] {y:6d} (Not in OEIS)")
                if first_oeis_found:
                    differences.append(y)  # track differences after alignment
        else:
            print(f"[{idx:6d}] {y:6d}")  # offline, just show computed y

    # --- Final report ---
    print("\n=== Summary ===")
    if oeis_data is not None:
        if initial_offset > 0:
            print(f"Initial offset before first OEIS match: {initial_offset} value(s)")
        else:
            print("No initial offset; first computed max_y is in OEIS")

        if differences:
            print(f"Differences found (computed max_y not in OEIS after alignment): {differences}")
        else:
            if initial_offset > 0:
                print("No differences found; all computed max_y values match OEIS sequence after initial offset")
            else:
                print("No differences found; all computed max_y values match OEIS sequence")
    else:
        print("OEIS comparison skipped (offline or unreachable)")


def main():
    n_end = 10000

    oeis_url = "https://oeis.org/A005563/b005563.txt"
    try:
        oeis_data = load_oeis_data(oeis_url)
    except RuntimeError as e:
        print(f"⚠️  {e}")
        print("Proceeding without OEIS comparison.\n")
        oeis_data = None

    run(n_end, oeis_data)


if __name__ == "__main__":
    main()
