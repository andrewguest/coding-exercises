import math


def parse_input(input_filename: str = "input.txt") -> list[str]:
    lines: list[str] = []

    with open(input_filename, "r") as file:
        lines = file.read().splitlines()

    return lines


def part_1(input_lines: list[str]):
    ways_to_beat_record = []
    races: list[dict[str, int]] = []

    for line in input_lines:
        if line.startswith("Time"):
            time_results = [int(t) for t in line.split(" ") if t.isdigit()]
        elif line.startswith("Distance"):
            distance_results = [int(d) for d in line.split(" ") if d.isdigit()]

    for race in range(1, len(time_results) + 1):
        races.append(
            {
                "race": race,
                "time": time_results[race - 1],
                "distance": distance_results[race - 1],
            }
        )

    for race in races:
        wins = 0
        race_time = race["time"]
        race_distance = race["distance"]

        for ms in range(1, race_time):
            if ms * (race_time - ms) > race_distance:
                wins += 1

        ways_to_beat_record.append(wins)

    print(math.prod(ways_to_beat_record))


def part_2(input_lines: list[str]):
    ways_to_beat_record = 0

    for line in input_lines:
        if line.startswith("Time"):
            time_result = int("".join([t for t in line.split(" ") if t.isdigit()]))
        elif line.startswith("Distance"):
            distance_result = int("".join([d for d in line.split(" ") if d.isdigit()]))

    for ms in range(1, time_result):
        if ms * (time_result - ms) > distance_result:
            ways_to_beat_record += 1

    print(ways_to_beat_record)


if __name__ == "__main__":
    question_input = parse_input()
    sample_input = parse_input("sample.txt")
    part_1(question_input)
    part_2(question_input)
