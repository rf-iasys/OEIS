n_max = 1000
numbers = list(range(1, n_max + 1))
marked = set()

# Start with x = first unmarked number
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

print("Numbers that have been marked):")
print(list(marked))
