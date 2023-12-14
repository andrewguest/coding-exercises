largest_palidrome: int = 0
number = 100

while number < 1000:
    for second_number in range(
        100, 1000
    ):  # loop through all three digit numbers
        current_total = number * second_number

        # if the product is a palidrome and larger than largest_palidrome then update largest_palidrome
        if (
            current_total == int(str(current_total)[::-1])
            and current_total > largest_palidrome
        ):
            largest_palidrome = current_total

        second_number += 1

    number += 1

print(largest_palidrome)
