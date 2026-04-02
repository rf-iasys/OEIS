import requests

# -------------------------------
# Load OEIS b-file (value -> index)
# -------------------------------
def load_oeis_data(url: str) -> dict[int, int]:
    """
    Fetch the OEIS b-file from the given URL and parse it.
    
    Returns:
        oeis_data: dictionary mapping value -> index in OEIS sequence
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except Exception:
        raise RuntimeError("Failed to fetch OEIS data")

    oeis_data = {}
    for line in response.text.splitlines():
        line = line.strip()
        # Skip empty lines and comments
        if not line or line.startswith("#"):
            continue
        try:
            idx, val = line.split()
            idx, val = int(idx), int(val)
            if val not in oeis_data:
                oeis_data[val] = idx
        except ValueError:
            continue
    return oeis_data

# -------------------------------
# Generate Numbers a such that b and c exist with b <= a < c and a*(a+1) + b^2 = c^2.
# -------------------------------
def generate_a154708(n_max: int):
    """
    Generate positions of the patterns '1001' or '0110' in the Thue-Morse sequence.
    
    Approach:
        - Use a sieve-like method inspired by the A154708 sequence.
        - Start with the first numbers and mark numbers according to the 
          pattern detection rule in Thue-Morse.
        - The marked numbers correspond to the positions where the pattern occurs.
    
    Parameters:
        n_max (int): maximum number to consider
    
    Return:
        marked (list): positions where patterns occur (A154708)
    """
    numbers = list(range(1, n_max + 1))
    marked = set()

    x_index = 0

    while x_index < len(numbers):
        x = numbers[x_index]
        marked_number = x + 2
        if marked_number > n_max:
            break
        marked.add(marked_number)
        
        # Find next x: first number > x that is not marked
        next_x_index = x_index + 1
        while next_x_index < len(numbers) and numbers[next_x_index] in marked:
            next_x_index += 1
        x_index = next_x_index

    return list(marked)

# -------------------------------
# Compare computed sequence with OEIS b-file
# -------------------------------
def compare_sequences(computed, oeis_data):
    """
    Compare the computed sequence to OEIS data, reporting matches and differences.
    
    Prints:
        - Index, value, and OEIS index if found
        - Summary with initial offset and mismatches
    """
    print("\n=== Comparison with OEIS A154708 ===\n")

    idx = 0
    first_match = False
    offset = 0
    differences = []

    for val in computed:
        idx += 1

        if val in oeis_data:
            oeis_idx = oeis_data[val]
            print(f"[{idx:4d}] {val:6d}  (OEIS a({oeis_idx}))")

            if not first_match:
                first_match = True
                offset = oeis_idx - idx + 1
        else:
            print(f"[{idx:4d}] {val:6d}  (NOT IN OEIS)")
            if first_match:
                differences.append(val)

    # Summary
    print("\n=== Summary ===")
    if first_match:
        print(f"Initial offset: {offset}")
    else:
        print("No matches found")

    if differences:
        print("Differences:", differences[:20], "..." if len(differences) > 20 else "")
    else:
        print("No differences after alignment")

# -------------------------------
# Main function
# -------------------------------
def main():
    n_max = 1000  # maximum value to generate

    # Generate numbers a such that b and c exist with b <= a < c and a*(a+1) + b^2 = c^2.
    marked = generate_a154708(n_max)

    print("Numbers a such that b and c exist with b <= a < c and a*(a+1) + b^2 = c^2 (first 50 terms):")
    print(marked[:50])

    # Load OEIS b-file for A154708
    url = "https://oeis.org/A154708/b154708.txt"
    oeis_data = load_oeis_data(url)

    # Compare the computed sequence with OEIS
    compare_sequences(marked, oeis_data)

if __name__ == "__main__":
    main()
