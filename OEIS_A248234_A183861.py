import requests

# --- Download OEIS A248234 ---
def load_oeis_a248234(url: str) -> list[int]:
    """
    Returns list of OEIS A248234 values (1-based indexing)
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except Exception:
        raise RuntimeError("Failed to fetch OEIS A248234 data")
    
    sequence = []
    for line in response.text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        try:
            idx = int(parts[0])
            value = int(parts[1])
            sequence.append(value)
        except ValueError:
            continue
    return sequence

# --- Compute your OEIS A193218 elements ---
def compute_elements(n_end: int) -> list[int]:
    """
    Compute elements using formula from OEIS A193218
    """
    elements = []
    for a in range(0, n_end):
        for b in range(a + 1, n_end - a + 1):
            x = abs(a**2 - b**2) * (a**3 + b**3)
            y = x * (b - a)
            if y != 0 and y == x:
                elements.append(y)
    # Sort and remove duplicates if any
    return sorted(list(set(elements)))

# --- OEIS A183861 computation ---
def compute_a183861(n: int) -> int:
    """
    OEIS A183861 formula for absolute difference:
    a(1) = 1; for n>1, a(n) = n-1 + ceil((n^2-1)/3)
    """
    if n == 1:
        return 1
    return (n - 1) + ((n**2 - 1 + 2) // 3)  # ceiling division

# --- Compare computed elements with OEIS A248234 ---
def compare_to_oeis(computed: list[int], oeis: list[int]) -> None:
    # --- Detect initial offset ---
    offset = 0
    for i, val in enumerate(computed):
        if i < len(oeis) and val == oeis[0]:
            offset = i
            break

    print(f"Detected initial offset: {offset} (computed index {offset+1} matches first OEIS value)\n")

    print(f"{'Index':>5} | {'Computed':>12} | {'OEIS A248234':>12} | {'Diff':>6} | {'A183861 (Formula)':>20}")
    print("-"*80)
    
    first_diff_index = None

    for idx, oeis_val in enumerate(oeis, start=1):
        computed_idx = idx - 1 + offset
        if computed_idx < len(computed):
            elem = computed[computed_idx]
            diff = elem - oeis_val

            # Adjust A183861 index correctly by subtracting 2 (to adjust for both the offset and the 1-based index)
            # Make sure the A183861 value is valid
            a183861_val = compute_a183861(idx - 1) if (idx - 1) > 0 else 'N/A'
            
            # Handle different types (int or 'N/A') in the print statement
            if isinstance(a183861_val, int):
                print(f"{idx:5d} | {elem:12d} | {oeis_val:12d} | {diff:6d} | {a183861_val:20d}")
            else:
                print(f"{idx:5d} | {elem:12d} | {oeis_val:12d} | {diff:6d} | {a183861_val:20s}")
            
            if diff != 0 and first_diff_index is None:
                first_diff_index = idx
        else:
            print(f"{idx:5d} | {'N/A':>12} | {oeis_val:12d} | {'-':>6} | {'-':>20}")
            if first_diff_index is None:
                first_diff_index = idx

    print("\n=== Summary ===")
    if first_diff_index:
        print(f"First mismatch at index {first_diff_index} (after applying offset)")
    else:
        print("All computed values match OEIS by index")

# --- Main ---
def main():
    n_end = 4002  # adjust as needed

    print("Computing elements from your formula (A193218)...")
    computed_elements = compute_elements(n_end)

    print(f"Downloading OEIS A248234 online...")
    oeis_url = "https://oeis.org/A248234/b248234.txt"
    try:
        oeis_sequence = load_oeis_a248234(oeis_url)
    except RuntimeError as e:
        print(f"⚠️ {e}")
        return

    print("\n=== Comparison ===\n")
    compare_to_oeis(computed_elements, oeis_sequence)

if __name__ == "__main__":
    main()
