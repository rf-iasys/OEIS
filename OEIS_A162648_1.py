# -------------------------------
# Efficient generator for A162648 (sieve method)
# -------------------------------
def generate_a162648_sieve_gen(n_max):
    """
    Generate positions of patterns 1001 or 0110 in the Thue-Morse sequence
    using the sieve method, in a memory-efficient way.
    """
    x = -1
    marked_set = set()  # fast membership check

    while True:
        marked_number = 2 * (x + 1)
        if marked_number > n_max - 3:  # clip to match official upper bound
            break

        # yield the marked number
        yield marked_number
        marked_set.add(marked_number)

        # find next unmarked x
        x += 1
        while x in marked_set:
            x += 1


# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    n_max = 100_000_000  # Can increase to billions
    sieve_gen = generate_a162648_sieve_gen(n_max)

    # Take first 50 terms
    first_50 = [next(sieve_gen) for _ in range(50)]
    print("First 50 terms (sieve):", first_50)

    # Optional: count all terms up to n_max
    total_terms = sum(1 for _ in generate_a162648_sieve_gen(n_max))
    print("Total terms up to n_max:", total_terms)
