def part_1():
    choices = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors"
    }
    points = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
        "lost": 0,
        "draw": 3,
        "won": 6
    }

    rounds_totals = []

    with open("./input.txt", "r") as f:
        for line in f:
            # total for this round
            current_total = 0

            opponent, outcome = line.split(" ")
            opponent = choices[opponent.rstrip()]
            outcome = choices[outcome.rstrip()]

            current_total += points[outcome]

            if opponent == "rock":
                if outcome == "rock":
                    current_total += points["draw"]
                elif outcome == "paper":
                    current_total += points["won"]
                elif outcome == "scissors":
                    current_total += points["lost"]
            elif opponent == "paper":
                if outcome == "rock":
                    current_total += points["lost"]
                elif outcome == "paper":
                    current_total += points["draw"]
                elif outcome == "scissors":
                    current_total += points["won"]
            elif opponent == "scissors":
                if outcome == "rock":
                    current_total += points["won"]
                elif outcome == "paper":
                    current_total += points["lost"]
                elif outcome == "scissors":
                    current_total += points["draw"]

            rounds_totals.append(current_total)


    print(sum(rounds_totals))


def part_2():
    choices = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "lose",
        "Y": "draw",
        "Z": "win"
    }
    points = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
        "lose": 0,
        "draw": 3,
        "win": 6
    }
    what_to_pick = {
        "rock": {
            "win": "paper",
            "draw": "rock",
            "lose": "scissors"
        },
        "paper": {
            "win": "scissors",
            "draw": "paper",
            "lose": "rock"
        },
        "scissors": {
            "win": "rock",
            "draw": "scissors",
            "lose": "paper"
        },
    }

    rounds_totals = []

    with open("./input.txt", "r") as f:
        for line in f:
            # total for this round
            current_total = 0

            opponent, outcome_letter = line.split(" ")
            opponent = choices[opponent.rstrip()]
            outcome_word = choices[outcome_letter.rstrip()]

            current_total += points[outcome_word]

            your_hand = what_to_pick[opponent][outcome_word]

            current_total += points[your_hand]

            rounds_totals.append(current_total)


    print(sum(rounds_totals))


part_1()
part_2()
