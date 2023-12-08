def parse_input(input_filename: str = "input.txt") -> list[str]:
    lines: list[str] = []

    with open(input_filename, "r") as file:
        lines = file.read().splitlines()

    return lines


def part_1(input_lines: list[str]):
    total_points = 0

    for line in input_lines:
        card_points = 0

        winning_numbers, your_numbers = line.split(" | ")
        winning_numbers = winning_numbers.split(": ")[1].strip()
        winning_numbers = winning_numbers.split(" ")
        winning_numbers = [int(x) for x in winning_numbers if len(x) > 0]

        your_numbers = your_numbers.split(" ")
        your_numbers = [int(x) for x in your_numbers if len(x) > 0]

        for number in your_numbers:
            if number in winning_numbers and card_points == 0:
                card_points += 1
            elif number in winning_numbers and card_points > 0:
                card_points *= 2

        total_points += card_points

    print(total_points)


def part_2(input_lines: list[str]):
    total_won_cards = []

    for line in input_lines:
        won_cards = []

        winning_numbers, your_numbers = line.split(" | ")

        card_number, winning_numbers = winning_numbers.split(": ")
        card_number = card_number.strip("Card ")
        card_number = int(card_number)
        total_won_cards.append(card_number)

        winning_numbers = winning_numbers.split(" ")
        winning_numbers = [int(x) for x in winning_numbers if len(x) > 0]

        your_numbers = your_numbers.split(" ")
        your_numbers = [int(x) for x in your_numbers if len(x) > 0]

        occurances = total_won_cards.count(card_number)

        if card_number == 1 or occurances > 0:
            for number in your_numbers:
                if number in winning_numbers and len(won_cards) == 0:
                    won_cards.append(card_number + 1)
                elif number in winning_numbers and len(won_cards) > 0:
                    won_cards.append(won_cards[-1] + 1)

            if card_number == 1:
                total_won_cards.extend(won_cards)
            else:
                won_cards = won_cards * occurances
                total_won_cards.extend(won_cards)
        else:
            break

    print(len(total_won_cards))


if __name__ == "__main__":
    question_input = parse_input()
    sample_input = parse_input("sample.txt")
    part_1(question_input)
    part_2(question_input)
