# 1) Create a variable to contain the `max_elf_calories` we currently have
# 2) Create a temporary `current_calories_total` variable to hold the
#       current round's total of calories
# 3) Read `input.txt` line by line, stripping any trailing newline characters
# 4) If the current line in the text file is a blank newline, then we've reached
#       the end of an elf's list and it's time to check if the `current_calories_total`
#       is greater than `max_elf_calories`. If it IS then replace `max_elf_calories`
#       with `current_calories_total`.
# 5) Set `current_calories_total` to 0 and start the loop again for the next elf.

def part_1():
    max_elf_calories: int = 0

    with open("./input.txt", "r") as f:
        current_calories_total: int = 0

        for line in f:
            if line == "\n":
                if current_calories_total > max_elf_calories:
                    max_elf_calories = current_calories_total
                current_calories_total = 0
            else:
                current_calories_total += int(line)

    print(max_elf_calories)


def part_2():
    elf_calories: list[int] = []

    with open("./input.txt", "r") as f:
        current_calories_total: int = 0

        for line in f:
            if line == "\n":
                elf_calories.append(current_calories_total)
                current_calories_total = 0
            else:
                current_calories_total += int(line)

    elf_calories.sort(reverse=True)
    print(sum(elf_calories[:3]))


part_1()
part_2()
