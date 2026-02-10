"""
brute_max_y_streamer.py

Brute-force streaming computation of numbers x where max_y(x) = x 
using the combinatorial formula y = x * |b - a| with x = |b^2 - a^2|.

This version performs no validation and outputs results directly 
for numbers in a given range [n_start, n_end).

Intended for exploration of sequences like OEIS A065091 (odd primes), 
where the sequence of numbers output by this code should correspond 
to the odd primes in the selected range.
"""

import math

def compute_max_y(n_start: int, n_end: int) -> dict[int,int]:
    """Compute max_y(x) using the combinatorial formula; return as dict."""
    max_y_per_x = dict()
    n_isqrt = math.isqrt(n_end)
    for a in range(n_end // 2):
        for b in range(a + 1, a + 1 + n_isqrt):
            x = abs(a**2 - b**2)
            y = x * abs(b - a)
            if y == 0:
                continue
            # Only store x if it's within the desired range
            if n_start <= x < n_end:
                if y > max_y_per_x.get(x, 0):
                    max_y_per_x[x] = y
    return max_y_per_x

def run(n_start: int, n_end: int) -> None:
    max_y_per_x = compute_max_y(n_start, n_end)

    print(f"x → max_y(x) (numbers from {n_start} to {n_end}):\n")

    idx = 0
    for x in sorted(max_y_per_x.keys()):
        if x == 1:  # skip 1 if desired
            continue
        y = max_y_per_x[x]
        if y != x:
            continue
        idx += 1
        print(f"[{idx:6d}] {x:6d}")

    print(f"\n✅ Reached x ≥ {n_end}. All numbers in range have been streamed.\n")

def main():
    n_start = 10000
    n_end = n_start + 2000
    run(n_start, n_end)

if __name__ == "__main__":
    main()
