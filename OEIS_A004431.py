"""
OEIS_A004431.py

Checks against OEIS A004431 online sequence if available.
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


def compute_max_y(n_start: int, n_end: int) -> dict[int,int]:
    """
    Compute max_y(x) using the combinatorial formula; return as dict.
    """
    max_y_per_x = dict()
    n_isqrt = math.isqrt(n_end)
    for a in range(n_end // 2):
        for b in range(a + 1, a + 1 + n_isqrt):
            x = a**2 + b**2
            y = x * abs(x - (a + b)**2)

            if y == 0:
                continue
            if n_start <= x < n_end:
                if y > max_y_per_x.get(x, 0):
                    max_y_per_x[x] = y
    return max_y_per_x


def run(n_start: int, n_end: int, oeis_data: dict[int,int] | None = None) -> None:
    max_y_per_x = compute_max_y(n_start, n_end)

    print("\n=== OEIS A004431 ===")
    print("a(n) = n*(n+2) = (n+1)^2 - 1\n")
    print(f"x → max_y(x) (numbers from {n_start} to {n_end}):\n")

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
            if x in oeis_data:
                oeis_index = oeis_data[x]
                print(f"[{idx:6d}] {x:6d} (OEIS: a({oeis_index}) = {x})")
                if not first_oeis_found:
                    first_oeis_found = True
                    initial_offset = idx - 1  # count of leading x not in OEIS
            else:
                print(f"[{idx:6d}] {x:6d} (Not in OEIS)")
                if first_oeis_found:
                    differences.append(x)  # track differences after alignment
        else:
            print(f"[{idx:6d}] {x:6d}")  # offline, just show computed x

    # --- Final report ---
    print("\n=== Summary ===")
    if oeis_data is not None:
        if initial_offset > 0:
            print(f"Initial offset before first OEIS match: {initial_offset} value(s)")
        else:
            print("No initial offset; first computed x is in OEIS")

        if differences:
            print(f"Differences found (computed x not in OEIS after alignment): {differences}")
        else:
            print("No differences found; all computed x match OEIS sequence after initial offset")
    else:
        print("OEIS comparison skipped (offline or unreachable)")


def main():
    n_start = 0
    n_end = n_start + 1000

    oeis_url = "https://oeis.org/A004431/b004431.txt"
    try:
        oeis_data = load_oeis_data(oeis_url)
    except RuntimeError as e:
        print(f"⚠️  {e}")
        print("Proceeding without OEIS comparison.\n")
        oeis_data = None

    run(n_start, n_end, oeis_data)


if __name__ == "__main__":
    main()
