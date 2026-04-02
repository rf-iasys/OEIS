# -------------------------------
# Efficient generator for A047311 (sieve method)
# -------------------------------
def generate_sieve_gen(n_max):
    x = 1
    marked_set = set()  # fast membership check

    while True:
        marked_number = x + 3
        if marked_number > n_max:
            break

        # yield the marked number
        yield marked_number
        marked_set.add(marked_number)

        # find next unmarked x
        x += 1
        while x in marked_set:
            x += 2


# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    n_max = 1000  # Can increase to billions
    sieve_gen = generate_sieve_gen(n_max)

    # Take first 50 terms
    first_50 = [next(sieve_gen) for _ in range(50)]
    print("First 50 terms (sieve):", first_50)

    # Optional: count all terms up to n_max
    total_terms = sum(1 for _ in generate_sieve_gen(n_max))
    print("Total terms up to n_max:", total_terms)
