# Starting list of random numbers
numbers_list = [5, 2, 8, 5, 1, 2, 9, 3, 8, 4]

# Create a dictionary where the `key` is the number from numbers_list and the
#   `value` is that numbers frequency in numbers_list
numbers_frequency = {num: numbers_list.count(num) for num in numbers_list}

# Find the max frequency value from the dictionary
max_frequency = max(numbers_frequency.values())

# Find the keys that match the `max_frequency` value and save the keys to a list
most_frequent_numbers = [str(k) for k, v in numbers_frequency.items() if v==max_frequency]
# Sort the list of keys in ascending order
most_frequent_numbers.sort()

# Print the results
print(f"Most frequent number(s): {', '.join(most_frequent_numbers)}")
print(f"Frequency: {max_frequency}")

