import math

# --------------------------
# Your sieve
# --------------------------
def sieve_simulation(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(current)
        k += math.floor(current/k)**2 + current + k
        current += k

    return marked

# --------------------------
# True A035344 via recurrence
# --------------------------
def generate_a035344(n):
    seq = []
    if n >= 1:
        seq.append(1)  # a(0)
    if n >= 2:
        seq.append(5)  # a(1)
    
    for i in range(2, n):
        next_val = 4*seq[i-1] - 2*seq[i-2] + 1
        seq.append(next_val)
    
    return seq

# --------------------------
# Comparison test
# --------------------------
def compare_sequences(n):
    sieve_seq = sieve_simulation(n)
    true_seq = generate_a035344(n)

    if sieve_seq == true_seq:
        print(f"All {n} terms match exactly!")
    else:
        print(f"There are mismatches in the first {n} terms.")

# --------------------------
# Run comparison for first 100000 terms
# --------------------------
compare_sequences(100000)
