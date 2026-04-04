import math

def sieve_simulation(n):
    marked = []
    current = 1
    k = 2

    while len(marked) < n:
        marked.append(current+1)
        k += math.floor(current/(k-1))
        current += k  # advance by how many have been marked

    return marked

# Example
print(sieve_simulation(1000))
