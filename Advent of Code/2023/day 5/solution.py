def parse_input(input_filename: str = "input.txt") -> list[str]:
    lines: list[str] = []

    with open(input_filename, "r") as file:
        lines = file.read().splitlines()

    return lines


def part_1(input_lines):
    ...


if __name__ == "__main__":
    sample_input = parse_input("sample.txt")
    question_input = parse_input()
