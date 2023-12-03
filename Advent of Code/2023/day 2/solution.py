def parse_input(input_filename: str = "input.txt") -> list[str]:
    lines: list[str] = []

    with open(input_filename, "r") as file:
        lines = file.readlines()

    return lines


def part_1(input_lines):
    game_id_sums = 0

    for game in input_lines:
        color_counts = {"blue": 0, "green": 0, "red": 0}

        game = game.strip()
        game_id = int(game.split(": ")[0].split(" ")[1])
        handfuls = game.split(": ")[1].split("; ")

        for handful_result in handfuls:
            draw = handful_result.split(", ")
            for d in draw:
                count = int(d.split(" ")[0])
                color = d.split(" ")[1]

                if count > color_counts[color]:
                    color_counts[color] = count

        if (
            color_counts["blue"] <= 14
            and color_counts["green"] <= 13
            and color_counts["red"] <= 12
        ):
            game_id_sums += game_id

    print(game_id_sums)


if __name__ == "__main__":
    input = parse_input()
    part_1(input)
