def parse_input(input_filename: str = "input.txt") -> list[str]:
    lines: list[str] = []

    with open(input_filename, "r") as file:
        lines = file.read().splitlines()

    return lines


def part_1(input_lines):
    """
    1. Subtract the smallest value in `left_numbers` from the smallest value in `right_numbers`.
    2. Store the difference in `differences`.
    3. Remove the smallest values from both lists.
    4. Repeat until both lists are empty
    """

    difference: int = 0
    left_numbers: list[int] = []
    right_numbers: list[int] = []

    for line in input_lines:
        left_temp, right_temp = line.split("   ")
        left_numbers.append(int(left_temp))
        right_numbers.append(int(right_temp))

    left_numbers.sort()
    right_numbers.sort()

    while left_numbers and right_numbers:
        difference += abs(right_numbers[0] - left_numbers[0])

        left_numbers = left_numbers[1:]
        right_numbers = right_numbers[1:]

    print(f"Part 1: {difference}")


def part_2(input_lines):
    similarity_total: int = 0

    left_numbers: list[int] = []
    right_numbers: list[int] = []

    for line in input_lines:
        left_temp, right_temp = line.split("   ")
        left_numbers.append(int(left_temp))
        right_numbers.append(int(right_temp))

    for number in left_numbers:
        similarity_total += number * right_numbers.count(number)

    print(f"Part 2: {similarity_total}")


if __name__ == "__main__":
    question_input = parse_input()
    part_1(question_input)
    part_2(question_input)
