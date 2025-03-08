input_list: list[int] = [3, 5, 8, 12, 22, 12, 3, 18, 3, 20]

# Easy
# Convert the list to a set, because sets can only contain unique values
print(f"Unique values: {set(input_list)}")

# Hard(er)
# Find the unique values manually
unique_values = []
for number in input_list:
    if number not in unique_values:
        unique_values.append(number)

print(f"Unique values: {unique_values}")
