import math

def sieve_simulation(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(2*current)
        k += math.floor(current/(k+1))
        current += k  # advance by how many have been marked

    return marked

# Example
print(sieve_simulation(1000))
