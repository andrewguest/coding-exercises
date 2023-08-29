import * as fs from "fs";

function day_1() {
    const choices: { [index: string]: string } = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors"
    };
    const points: { [index: string]: number } = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
        "lost": 0,
        "draw": 3,
        "won": 6
    };

    let round_totals: number[] = [];
    const input = fs.readFileSync("./input.txt", "utf-8");
    const input_array = input.split("\n");

    for (let index = 0; index < input_array.length; index++) {
        const element = input_array[index];

        let opponent: string = element.split(" ")[0];
        opponent = choices[opponent];

        let you: string = element.split(" ")[1];
        you = choices[String(you)];

        let current_round_total: number = 0;
        current_round_total += points[you];

        if (opponent == "rock") {
            if (you == "rock") {
                current_round_total += points["draw"];
            } else if (you == "paper") {
                current_round_total += points["won"];
            } else if (you == "scissors") {
                current_round_total += points["lost"];
            }
        } else if (opponent == "paper") {
            if (you == "rock") {
                current_round_total += points["lost"];
            } else if (you == "paper") {
                current_round_total += points["draw"];
            } else if (you == "scissors") {
                current_round_total += points["won"];
            }
        } else if (opponent == "scissors") {
            if (you == "rock") {
                current_round_total += points["won"];
            } else if (you == "paper") {
                current_round_total += points["lost"];
            } else if (you == "scissors") {
                current_round_total += points["draw"];
            }
        }

        round_totals.push(current_round_total);
    }

    console.log(round_totals.reduce((a, b) => a + b, 0));
}


function day_2() {
    const choices: { [index: string]: string } = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "lose",
        "Y": "draw",
        "Z": "win"
    };
    const points: { [index: string]: number } = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
        "lose": 0,
        "draw": 3,
        "win": 6
    };
    const what_to_pick: { [index: string]: { [index: string]: string } } = {
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
    };

    let round_totals: number[] = [];
    const input = fs.readFileSync("./input.txt", "utf-8");
    const input_array = input.split("\n");

    for (let index = 0; index < input_array.length; index++) {
        const element = input_array[index];

        let opponent: string = element.split(" ")[0];
        opponent = choices[opponent];

        const outcome_letter: string = element.split(" ")[1];
        const outcome_word = choices[String(outcome_letter)];

        let current_round_total: number = 0;

        current_round_total += points[outcome_word];

        const your_hand = what_to_pick[opponent][outcome_word];
        current_round_total += points[your_hand];

        round_totals.push(current_round_total);
    }

    console.log(round_totals.reduce((a, b) => a + b, 0));
}


day_1();
day_2();
