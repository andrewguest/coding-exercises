def parse_input(input_filename: str = "input.txt") -> list[str]:
    lines: list[str] = []

    with open(input_filename, "r") as file:
        lines = file.readlines()

    return lines


def day_1(input_lines):
    """
    Loop through each line of input.txt and combine the first and last digit
        to form a single two-digit number. Then SUM all of the two-digit numbers
        together and return the final total.
    For example:
        `1abc2` becomes `12`
        `ab3gt52f4x` becomes `34`

        The total would be 12 + 34 = 46
    """

    numbers: list[int] = []

    for line in input_lines:
        digits = [x for x in line if x.isdigit()]
        if len(digits) < 2:
            numbers.append(int(digits[0] * 2))
        else:
            numbers.append(int(digits[0] + digits[-1]))

    print(sum(numbers))


if __name__ == "__main__":
    question_input = parse_input()
    day_1(question_input)
