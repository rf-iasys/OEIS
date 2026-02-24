"""
Local verification version.

- Replaces OEIS A005563 with formula: a(n) = n(n+2) = (n+1)^2 - 1
- Generates A276382 indices from matches.
- Compares generated A276382 with official OEIS sequence.
"""

import math
import requests


# --------------------------
# Check if value is in A005563
# --------------------------
def is_A005563_value(x: int) -> tuple[bool, int | None]:
    s = int(math.isqrt(x + 1))
    if s * s == x + 1:
        n = s - 1
        if n >= 1:
            return True, n
    return False, None


# --------------------------
# Generate A276382
# --------------------------
def generate_a276382(n_terms: int) -> list[int]:
    if n_terms <= 0:
        return []
    seq = [1]
    for n in range(2, n_terms + 1):
        seq.append(seq[-1] + (3 * n) // 2 + 1)
    return seq


# --------------------------
# Compute max_y(x)
# --------------------------
def compute_max_y(n_start: int, n_end: int) -> dict[int, int]:
    max_y_per_x = {}
    for a in range(0, n_end // 2):
        for b in range(a + 1, n_end - a + 1):
            x = abs(a*a - b*b)
            y = x * abs(a + b)
            if y == 0 or x < n_start or x >= n_end:
                continue
            if y > max_y_per_x.get(x, 0):
                max_y_per_x[x] = y
    return max_y_per_x


# --------------------------
# Compare with OEIS A276382
# --------------------------
def compare_with_oeis(local_seq: list[int]) -> None:
    url = "https://oeis.org/A276382/b276382.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        oeis_data = response.text.split()
        oeis_values = [int(oeis_data[i]) for i in range(1, len(oeis_data), 2)]
    except Exception as e:
        print(f"Error fetching OEIS data: {e}")
        return

    mismatches = [(i+1, local_seq[i], oeis_values[i])
                  for i in range(min(len(local_seq), len(oeis_values)))
                  if local_seq[i] != oeis_values[i]]

    print("\n=== OEIS Comparison ===")
    if mismatches:
        print(f"Mismatches ({len(mismatches)}): index | local | OEIS")
        for idx, local_val, oeis_val in mismatches:
            print(f"{idx:5} | {local_val:5} | {oeis_val:5}")
    else:
        print("All local values match OEIS sequence.")


# --------------------------
# Main runner
# --------------------------
def run(n_start: int, n_end: int) -> None:
    max_y_per_x = compute_max_y(n_start, n_end)
    match_counter = 0

    # Collect matches and generate A276382 indices
    a276382_seq = []
    for x in sorted(max_y_per_x.keys()):
        if x == 1:
            continue
        is_match, _ = is_A005563_value(x)
        if is_match:
            match_counter += 1
            if len(a276382_seq) < match_counter:
                a276382_seq = generate_a276382(match_counter)

    # --------------------------
    # Report
    # --------------------------
    print("\n=== Summary ===")
    print(f"Total A005563 matches: {match_counter}")
    if match_counter:
        print("Generated A276382 indices:")
        print(a276382_seq[:match_counter])

    compare_with_oeis(a276382_seq[:match_counter])


# --------------------------
# Main
# --------------------------
if __name__ == "__main__":
    run(n_start=0, n_end=100000)
