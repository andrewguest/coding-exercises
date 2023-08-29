import * as fs from "fs";

function day_1() {
    let total: number = 0;

    const input = fs.readFileSync("./input.txt", "utf-8");
    const input_array = input.split("\n");

    for (let index = 0; index < input_array.length; index++) {
        let duplicate_items: string[] = [];

        const element = input_array[index];
        const first_rucksack = element.substring(0, (element.length / 2));
        const second_rucksack = element.substring((element.length / 2), element.length);

        // Check if each letter of `first_rucksack` is in `second_rucksack` and not in `duplicate_items
        for (let letter_index = 0; letter_index < first_rucksack.length; letter_index++) {
            const f = first_rucksack[letter_index];

            if (second_rucksack.includes(f) && !duplicate_items.includes(f)) {
                duplicate_items.push(f);
            }
        }

        for (let index = 0; index < duplicate_items.length; index++) {
            const element = duplicate_items[index];

            if (element == element.toLowerCase()) {
                total += element.charCodeAt(0) - 96
            } else {
                total += element.charCodeAt(0) - 38
            }
        }
    }

    console.log(total);
}


function day_2() {
    let total: number = 0;
    let badge_characters: string[] = [];
    let starting_index = 0;
    let ending_index = 2;

    const input = fs.readFileSync("./input.txt", "utf-8");
    const lines_in_file = input.split("\n");

    while (ending_index <= lines_in_file.length) {
        let first_line = lines_in_file[starting_index];
        let second_line = lines_in_file[starting_index + 1];
        let third_line = lines_in_file[ending_index];

        for (let index = 0; index < first_line.length; index++) {
            const element = first_line[index];

            if ((second_line.includes(element)) && (third_line.includes(element))) {
                badge_characters.push(element);
                break;
            }
        }
        starting_index += 3;
        ending_index += 3;
    }

    for (let index = 0; index < badge_characters.length; index++) {
        const element = badge_characters[index];

        if (element == element.toLowerCase()) {
            total += element.charCodeAt(0) - 96
        } else {
            total += element.charCodeAt(0) - 38
        }
    }

    console.log(total);
}


day_1();
day_2();
