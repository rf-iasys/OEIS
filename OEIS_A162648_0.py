# -------------------------------
# Official A162648 generation (Thue-Morse window method)
# -------------------------------
def thue_morse(n_max):
    t = [0] * n_max
    for n in range(1, n_max):
        t[n] = 1 - t[n // 2] if n % 2 else t[n // 2]
    return t

def generate_a162648_official(n_max):
    t = thue_morse(n_max + 3)  # need window of 4 bits
    positions = []
    for i in range(n_max - 3):
        window = t[i:i+4]
        if window == [1,0,0,1] or window == [0,1,1,0]:
            positions.append(i)
    return positions

# -------------------------------
# Sieve method for A162648
# -------------------------------
def generate_a162648_sieve(n_max):
    numbers = list(range(-1, n_max + 1))
    marked_set = set()   # For fast membership check
    marked_list = []     # For maintaining order

    x_index = 0
    while x_index < len(numbers):
        x = numbers[x_index]
        marked_number = 2 * (x + 1)
        
        if marked_number > n_max - 3:  # clip to match official upper bound
            break

        # append in order, mark in set for fast check
        marked_list.append(marked_number)
        marked_set.add(marked_number)

        # Find next unmarked number > x
        next_x_index = x_index + 1
        
        while next_x_index < len(numbers) and numbers[next_x_index] in marked_set:
            next_x_index += 1

        x_index = next_x_index

    return marked_list

# -------------------------------
# Compare sequences
# -------------------------------
def compare_sequences(seq1, seq2):
    set1 = set(seq1)
    set2 = set(seq2)

    in_seq1_not_seq2 = list(set1 - set2)
    in_seq2_not_seq1 = list(set2 - set1)

    print(f"Total terms in seq1: {len(seq1)}")
    print(f"Total terms in seq2: {len(seq2)}")
    print()
    if not in_seq1_not_seq2 and not in_seq2_not_seq1:
        print("✅ Both sequences match exactly!")
    else:
        print("❌ Sequences differ!")
        if in_seq1_not_seq2:
            print("Terms in seq1 not in seq2:", in_seq1_not_seq2[:20], "...")
        if in_seq2_not_seq1:
            print("Terms in seq2 not in seq1:", in_seq2_not_seq1[:20], "...")

# -------------------------------
# Main
# -------------------------------
def main():
    n_max = 100000000  # Can change this to any number

    official = generate_a162648_official(n_max)
    sieve = generate_a162648_sieve(n_max)

    print("First 50 terms (official):", official[:50])
    print("First 50 terms (sieve):   ", sieve[:50])
    print()

    # Compare
    compare_sequences(official, sieve)

if __name__ == "__main__":
    main()
