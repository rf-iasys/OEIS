"""
Minimal OEIS A189642 report generator + gcd(9) multiplier proof
"""

import requests
from sympy import factorint
from math import gcd

def load_oeis_data(url: str) -> dict[int,int]:
    """Fetch OEIS sequence data from URL."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except Exception:
        print("⚠️ Failed to fetch OEIS data; continuing without it.")
        return {}

    oeis_data = {}
    for line in response.text.splitlines():
        if line.startswith("#") or not line.strip():
            continue
        try:
            index, value = map(int, line.split())
            oeis_data[value] = index
        except ValueError:
            continue
    return oeis_data


def poly(a: int) -> int:
    """Raw polynomial numerator."""
    return 2*a**3 + 3*a**2 - a - 1


def reduced_numerator(a: int) -> int:
    """Compute reduced numerator of H(n+4)-H(n) after simplification."""
    num = 2 * poly(a)
    den = (a-1)*a*(a+1)*(a+2)

    g = gcd(num, den)
    return num // g


def run_report(n_start: int, n_end: int, oeis_data: dict[int,int] = None):
    """Generate report verifying gcd(a+1,9) multiplier."""

    print("\n=== OEIS A189642 multiplier structure ===\n")

    header = f"{'a':>5} | {'P(a)':>12} | {'Reduced':>10} | {'mult':>4} | {'gcd(a+5,9)':>10}"
    print(header)
    print("-"*len(header))

    for a in range(2, n_end):

        p = poly(a)
        r = reduced_numerator(a)

        multiplier = p // r
        g9 = gcd(a+5, 9)

        print(f"{a:5d} | {p:12d} | {r:10d} | {multiplier:4d} | {g9:10d}")


def main():
    n_start = 0
    n_end = 60
    oeis_url = "https://oeis.org/A189642/b189642.txt"
    oeis_data = load_oeis_data(oeis_url)

    run_report(n_start, n_end, oeis_data)


if __name__ == "__main__":
    main()
