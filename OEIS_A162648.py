# -------------------------------
# Sieve method for A162648
# -------------------------------
def generate_a162648_sieve(n_max):
    """
    Generate positions of patterns '1001' or '0110' in the Thue-Morse sequence
    using the sieve method (order-preserving).

    Algorithm:
      1. Start with numbers = -1..n_max
      2. Initialize an empty list (marked_list) and set (marked_set)
      3. For x = first unmarked number:
           mark 2*(x+1) (append to marked_list and marked_set)
      4. Repeat with the next unmarked number > x
      5. Stop when 2*(x+1) exceeds n_max - 3
      6. Return marked_list, which preserves order and matches official sequence
    """
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

# Example usage:
n_max = 1000
seq = generate_a162648_sieve(n_max)
print(seq[:50])
