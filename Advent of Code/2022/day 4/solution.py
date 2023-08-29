def read_input_file(filepath: str = "./input.txt") -> list[str]:
    file_lines: list[str] = []

    with open(filepath, "r") as f:
        for line in f:
            file_lines.append(line.rstrip())

    return file_lines


def day_1():
    file_lines: list[str] = read_input_file()
    fully_contained_pairs = 0

    for line in file_lines:
        first, second = line.split(",")

        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")

        if first_start != first_end:
            first = [x for x in range(int(first.split("-")[0]), int(first.split("-")[1]) + 1)]
        else:
            first = [int(first_start)]

        if second_start != second_end:
            second = [x for x in range(int(second.split("-")[0]), int(second.split("-")[1]) + 1)]
        else:
            second = [int(second_start)]

        if first == second:
            fully_contained_pairs += 1
        elif all(item in first for item in second):
            fully_contained_pairs += 1
        elif all(item in second for item in first):
            fully_contained_pairs += 1
        else:
            pass

    print(fully_contained_pairs)


day_1()
