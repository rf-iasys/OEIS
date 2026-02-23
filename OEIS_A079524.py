import math
import requests

# ---------------- Utilities ----------------
def is_perfect_square(n: int) -> bool:
    root = int(math.isqrt(n))
    return root * root == n

def load_oeis_data(url: str) -> set[int]:
    """Load OEIS A079524 sequence as a set of indices."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except Exception:
        raise RuntimeError("Failed to fetch OEIS data (offline or URL unreachable)")

    indices = set()
    for line in response.text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            idx, value = line.split()
            indices.add(int(value))
        except ValueError:
            continue
    return indices

# ---------------- Combinatorial sequence ----------------
def compute_max_y(n_start: int, n_limit: int) -> dict[int,int]:
    """Compute max y(x) up to n_limit to reduce memory."""
    max_y = {}
    n_limit_isqrt = math.isqrt(n_limit)
    for a in range(0, n_limit_isqrt):
        for b in range(a + 1, n_limit - a + 1):
            x = a * b - a - b
            if x < n_start or x == 1:
                continue
            y = x * abs(a*a + b)
            if y > max_y.get(x, 0):
                max_y[x] = y
    return max_y

def generate_a079524_indices(n_start: int, n_end: int) -> list[int]:
    """
    Compute A079524 indices from combinatorial sequence:
    indices where y + 9 is NOT a perfect square, stopping at index n_end.
    """
    max_y = compute_max_y(n_start, n_end*2)  # generate enough values
    a079524_indices = []
    idx = 0
    for x in sorted(max_y.keys()):
        value = max_y[x]
        idx += 1
        if idx > n_end:  # stop at index limit
            break
        if not is_perfect_square(value + 9):
            a079524_indices.append(idx)
    return a079524_indices

# ---------------- Validation against OEIS ----------------
def validate_a079524_indices(computed_indices: list[int], oeis_url: str):
    try:
        oeis_data = load_oeis_data(oeis_url)
    except RuntimeError as e:
        print(f"⚠️  {e}")
        return

    # Report mismatches
    mismatches = [idx for idx in computed_indices if idx not in oeis_data]
    print(f"\n=== OEIS A079524 Validation ===")
    print(f"Computed indices count: {len(computed_indices)}")
    if not mismatches:
        print("✅ All computed indices match OEIS A079524")
    else:
        print(f"❌ Mismatching indices (not in OEIS): {mismatches}")

# ---------------- Main ----------------
def main():
    n_start = 0
    n_end = 300000  # limit for indices

    # Generate indices
    a079524_indices = generate_a079524_indices(n_start, n_end)
    print(f"A079524 indices up to n_end={n_end}:")
    print(a079524_indices)

    # Validate against OEIS
    oeis_url = "https://oeis.org/A079524/b079524.txt"
    validate_a079524_indices(a079524_indices, oeis_url)

if __name__ == "__main__":
    main()
