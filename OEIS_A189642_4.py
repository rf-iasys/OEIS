"""
Rebuild OEIS A189642 from the cubic polynomial

A189642(a-2) = (2*a^3 + 3*a^2 - a - 1) / gcd(a+5, 9)
"""

from math import gcd
import requests


def cubic(a: int) -> int:
    """Cubic polynomial."""
    return 2*a**3 + 3*a**2 - a - 1


def rebuild_A189642(n_terms: int):
    """
    Rebuild A189642 using the cubic and gcd factor.
    a starts at 2 so that index alignment matches OEIS.
    """
    seq = []

    for a in range(2, n_terms + 2):
        P = cubic(a)
        g = gcd(a + 5, 9)
        value = P // g
        seq.append(value)

    return seq


def load_oeis(url: str):
    """Fetch OEIS reference data for comparison."""
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
    except Exception:
        print("⚠️ Could not fetch OEIS data")
        return {}

    data = {}
    for line in r.text.splitlines():
        if line.startswith("#") or not line.strip():
            continue
        i, v = map(int, line.split())
        data[i] = v
    return data


def verify(seq, oeis):
    """Compare rebuilt sequence with OEIS."""
    print(f"{'n':>5} | {'Rebuilt':>10} | {'OEIS':>10} | Check")

    for i, val in enumerate(seq, 0):
        ref = oeis.get(i)
        ok = "✓" if ref == val else "✗"
        print(f"{i:5d} | {val:10d} | {ref if ref else 0:10d} | {ok}")


def main():

    n = 1000

    seq = rebuild_A189642(n)

    print("\nFirst 100 terms rebuilt:")
    print(seq[:100])

    oeis_url = "https://oeis.org/A189642/b189642.txt"
    oeis = load_oeis(oeis_url)

    if oeis:
        print("\nVerification with OEIS:")
        verify(seq, oeis)


if __name__ == "__main__":
    main()
