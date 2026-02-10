"""
OEIS_A065091.py

Checks against OEIS A065091 online sequence if available.
Reports initial offset, any differences, and validates results
against actual primality.

This algorithm generates exactly the odd primes in a given range
using a combinatorial fixed-point condition, without using sieves
or explicit primality tests in the generation phase.

Flags:
- stop_at_n_end: stop computing once x reaches n_end
- use_y_values: if True, report max_y(x) values; if False, report x values
"""

import math
import requests


def load_oeis_data(url: str) -> dict[int, int]:
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
                  stop_at_n_end: bool = True) -> dict[int, int]:
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
            x = abs(a**2 - b**2)
            y = x * abs(b - a)

            if y == 0 or x < n_start:
                continue

            if stop_at_n_end and x >= n_end:
                continue

            if y > max_y_per_x.get(x, 0):
                max_y_per_x[x] = y

    return max_y_per_x


def sieve_primes(limit: int) -> list[bool]:
    """Return a boolean list where True means prime."""
    if limit < 2:
        return [False] * (limit + 1)

    is_prime = [False, False] + [True] * (limit - 1)
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime


def run(n_start: int, n_end: int, oeis_data: dict[int, int] | None = None,
        stop_at_n_end: bool = True, use_y_values: bool = False) -> None:

    max_y_per_x = compute_max_y(n_start, n_end, stop_at_n_end=stop_at_n_end)

    print("\n=== OEIS A065091 ===")
    print("Odd primes\n")
    print(f"Numbers from {n_start} to {n_end} ({'max_y(x)' if use_y_values else 'x'}):\n")
    print(f"{'Index':>7}|{'Element':>7}| OEIS\n")

    idx = 0
    initial_offset = 0
    differences = []
    first_oeis_found = False

    found_numbers: list[int] = []

    for x in sorted(max_y_per_x.keys()):
        if x == 1:
            continue

        y = max_y_per_x[x]

        # 🔒 Fixed-point verification
        if y != x:
            continue

        idx += 1
        value_to_report = y if use_y_values else x
        found_numbers.append(value_to_report)

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
            print(f"Differences found (computed values not in OEIS after alignment): {differences}")
        else:
            print("No differences found; all computed values match OEIS sequence after initial offset")
    else:
        print("OEIS comparison skipped (offline or unreachable)")

    # --- Mathematical Validation ---
    print("\n=== Mathematical Validation ===")

    is_prime = sieve_primes(n_end)

    missing_primes = []
    composites_found = []

    for x in found_numbers:
        if x >= n_end or x == 2:
            continue
        if not is_prime[x]:
            composites_found.append(x)

    for p in range(max(3, n_start), n_end, 2):
        if is_prime[p] and p not in found_numbers:
            missing_primes.append(p)

    if missing_primes:
        print(f"❌ Missing odd primes: {len(missing_primes)}")
        print(f"First few missing primes: {missing_primes[:10]}")
    else:
        print("✔ No odd primes are missing")

    if composites_found:
        print(f"❌ Composites detected: {len(composites_found)}")
        print(f"First few composites: {composites_found[:10]}")
    else:
        print("✔ No composites detected")


def main():
    n_start = 0
    n_end = n_start + 10000

    # Flags
    stop_at_n_end = True
    use_y_values = False

    oeis_url = "https://oeis.org/A065091/b065091.txt"
    try:
        oeis_data = load_oeis_data(oeis_url)
    except RuntimeError as e:
        print(f"⚠️  {e}")
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
