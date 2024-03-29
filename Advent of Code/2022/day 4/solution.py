import re


def read_input_file(filepath: str = "./input.txt") -> list[str]:
    file_lines: list[str] = []

    with open(filepath, "r") as f:
        for line in f:
            file_lines.append(line.rstrip())

    return file_lines


def part_1() -> int:
    data = read_input_file()

    t = 0
    for line in data:
        a, b, c, d = map(int, re.findall(r"(\d+)", line))
        if (a >= c and b <= d) or (c >= a and d <= b):
            t += 1

    return t


def part_2() -> int:
    data = read_input_file()

    t = 0
    for line in data:
        a, b, c, d = map(int, re.findall(r"(\d+)", line))
        if (b >= c and b <= d) or (d >= a and d <= b):
            t += 1

    return t


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
