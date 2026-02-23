import requests
import sympy

def find_all_occurrences_of_value(url, target_value):
    # Fetch the file content from the given URL
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching the file.")
        return
    
    # Split the content into lines
    lines = response.text.splitlines()
    
    # List to hold all indices where the value matches the target_value
    indices = []
    
    # Iterate through each line, skipping comment lines
    for line in lines:
        if line.startswith("#"):
            continue  # Skip comment lines
        
        # Split the line into index and value
        parts = line.split()
        if len(parts) == 2:
            index, value = parts
            try:
                # Convert the index and value to integers
                index = int(index)
                value = int(value)
                
                # Check if the value matches the target value
                if value == target_value:
                    indices.append(index)  # Add the index to the list
            except ValueError:
                continue  # Skip lines that do not have valid integer values
    
    # If indices were found, return them
    if indices:
        print(f"Value {target_value} found at indices: {indices}")
        # Now verify if these indices are 12 times a prime number starting from 11
        verify_prime_indices(indices)
        return indices  # Return the list of indices
    else:
        print(f"Value {target_value} not found in the sequence.")
        return None  # If not found, return None

def verify_prime_indices(indices, start_prime=11):
    # Generate primes starting from the given start_prime
    primes = list(sympy.primerange(start_prime, 100000))  # Get a large range of primes
    
    # Multiply each prime by 12
    prime_times_12 = [12 * prime for prime in primes]
    
    # Check if all indices are in the prime_times_12 list
    mismatches = [index for index in indices if index not in prime_times_12]
    
    if mismatches:
        print(f"These indices are not 12 times a prime starting from {start_prime}: {mismatches}")
    else:
        print(f"All indices are 12 times a prime starting from {start_prime}.")

# URL of the b346242.txt file
url = 'https://oeis.org/A346242/b346242.txt'

# We are looking for the value +2
target_value = 2

# Call the function to find all occurrences of +2
find_all_occurrences_of_value(url, target_value)
