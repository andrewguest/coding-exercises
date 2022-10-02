var total = 0

for number in 1..999:
    if number mod 3 == 0 or number mod 5 == 0:
        total += number

echo(total)
