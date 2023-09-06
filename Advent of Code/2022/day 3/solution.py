def part_1():
    total = 0

    with open("./input.txt", "r") as f:
        for line in f:
            duplicate_items = []

            line = line.rstrip()
            first_rucksack = line[0:len(line)//2]
            second_rucksack = line[len(line)//2:]

            for f in first_rucksack:
                if f in second_rucksack and f not in duplicate_items:
                    duplicate_items.append(f)

            for letter in set(duplicate_items):
                if letter.islower():
                    total += (ord(letter) - 96)
                elif letter.isupper():
                    total += ord(letter) - 38

    print(total)


def part_2():
    total = 0
    badge_characters = []
    lines_in_file: list[str] = []
    starting_index = 0
    ending_index = 2

    with open("./input.txt", "r") as f:
        for line in f:
            lines_in_file.append(line.rstrip())

    while ending_index <= len(lines_in_file):
        first_line = lines_in_file[starting_index]
        second_line = lines_in_file[starting_index + 1]
        third_line = lines_in_file[ending_index]

        for character in first_line:
            if ( (character in second_line) and (character in third_line) ):
                badge_characters.append(character)
                break
            else:
                pass
        starting_index += 3
        ending_index += 3

    for letter in badge_characters:
        if letter.islower():
            total += (ord(letter) - 96)
        elif letter.isupper():
            total += ord(letter) - 38

    print(total)


part_1()
part_2()
