max_number: int = 1000
total: int | str = 0

for number in range(1, max_number + 1):
    total += number ** number

total = str(total)

print(total[len(total) - 10:])
