"""
Minimal OEIS A189642 report generator
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

def compute_sequence(n_start: int, n_end: int) -> list[int]:
    """Compute OEIS A189642 sequence using simplified formula x = 2a^3 + 3a^2 - a - 1."""
    return [2*a**3 + 3*a**2 - a - 1 for a in range(2, n_end)]

def run_report(n_start: int, n_end: int, oeis_data: dict[int,int] = None):
    """Generate report with OEIS comparison and prime factorization."""
    sequence = compute_sequence(n_start, n_end)

    print("\n=== OEIS A189642 ===")
    print("Numerator of H(n+4) - H(n), where H(n) = Sum_{k=1..n} 1/k.\n")
    print(f"{'Index':>7} | {'Element':>12} | OEIS | Factors")

    for idx, value in enumerate(sequence, 1):
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
