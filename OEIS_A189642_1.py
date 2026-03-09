"""
Simplified OEIS A189642 report generator
"""

import requests
from sympy import factorint

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

def compute_max_y(n_start: int, n_end: int) -> dict[int, int]:
    """Compute sequence values for x = |a^2 - b^2 + a*b*(a+b)|."""
    max_y_per_x = {}
    for a in range(2, n_end):
        b = a + 1
        #x = abs(a**2 - b**2 + a*b*(a+b)) 'Original formula.
        x = 2*a**3 + 3*a**2 -a -1
        max_y_per_x[x] = x
    return max_y_per_x

def run_report(n_start: int, n_end: int, oeis_data: dict[int,int] = None):
    """Generate report with OEIS comparison and factorization."""
    sequence = compute_max_y(n_start, n_end)

    print("\n=== OEIS A189642 ===")
    print("Numerator of H(n+4) - H(n), where H(n) = Sum_{k=1..n} 1/k.\n")
    print(f"{'Index':>7} | {'Element':>12} | OEIS | Factors")

    for idx, x in enumerate(sorted(sequence.keys()), 1):
        value = sequence[x]

        # Prime factorization
        factors = factorint(value)
        factors_str = " * ".join(
            f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(factors.items())
        )

        # OEIS check
        tag = "Not in OEIS"
        if oeis_data:
            if value in oeis_data:
                tag = f"a({oeis_data[value]})"
            elif value % 3 == 0 and (value // 3) in oeis_data:
                tag = f"3×a({oeis_data[value//3]})"
            elif value % 9 == 0 and (value // 9) in oeis_data:
                tag = f"9×a({oeis_data[value//9]})"

        print(f"[{idx:6d}] {value:12d} ({tag}) | {factors_str}")

def main():
    n_start = 0
    n_end = 1000
    oeis_url = "https://oeis.org/A189642/b189642.txt"
    oeis_data = load_oeis_data(oeis_url)
    run_report(n_start, n_end, oeis_data)

if __name__ == "__main__":
    main()
