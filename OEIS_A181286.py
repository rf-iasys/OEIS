import math

def sieve_simulation(n):
    marked = []
    current = 1
    k = 1

    while len(marked) < n:
        marked.append(current)
        k += math.floor((2*current)/k)
        current += k  # advance by how many have been marked

    return marked

# Example
print(sieve_simulation(1000))
