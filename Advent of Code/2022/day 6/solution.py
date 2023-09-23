def read_input_file(filepath: str = "./input.txt") -> list[str]:
    file_lines: list[str] = []

    with open(filepath, "r") as f:
        for line in f:
            file_lines.append(line.rstrip())

    return file_lines


def part_1() -> int:
    packet_start_index = None
    input_string = read_input_file()[0]
    start_index = 0
    end_index = 4

    # Loop until we have an answer
    while not packet_start_index:
        # Get the 4 characters we're currently checking
        current_substring = input_string[start_index:end_index]
        current_substring = [_ for _ in current_substring]

        # Check the substring for duplicates
        if len(current_substring) == len(set(current_substring)):
            packet_start_index = end_index
            break
        else:
            start_index += 1
            end_index += 1

    return packet_start_index


def part_2() -> int:
    message_start_index = None
    input_string = read_input_file()[0]
    start_index = 0
    end_index = 14

    # Loop until we have an answer
    while not message_start_index:
        # Get the 4 characters we're currently checking
        current_substring = input_string[start_index:end_index]
        current_substring = [_ for _ in current_substring]

        # Check the substring for duplicates
        if len(current_substring) == len(set(current_substring)):
            message_start_index = end_index
            break
        else:
            start_index += 1
            end_index += 1

    return message_start_index


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
