import * as fs from "fs";

function part_1() {
    const words = fs.readFileSync('./input.txt', 'utf-8');
    const words_array = words.split('\n');

    let max_elf_calories: number = 0;
    let current_calories_total: number = 0;

    for (let index = 0; index < words_array.length; index++) {
        const element = words_array[index];

        /* If the current line is a blank newline then we've reached a
            new elf so we check if `current_calories_total` is greater
            than `max_elf_calories`. If it is then set `max_elf_calories`
            to `current_calories_total`. Then set `current_calories_total` to 0.
        */
        if (element == '') {
            if (current_calories_total > max_elf_calories) {
                max_elf_calories = current_calories_total;
            }
            current_calories_total = 0;
        } else {
            current_calories_total += Number(element);
        }
    }

    console.log(max_elf_calories);
}


function part_2() {
    const words = fs.readFileSync('./input.txt', 'utf-8');
    const words_array = words.split('\n');

    let max_elf_calories: number[] = [];
    let current_calories_total: number = 0;

    for (let index = 0; index < words_array.length; index++) {
        const element = words_array[index];

        /* If the current line is a blank newline then we've reached a
            new elf so we check if `current_calories_total` is greater
            than `max_elf_calories`. If it is then set `max_elf_calories`
            to `current_calories_total`. Then set `current_calories_total` to 0.
        */
        if (element == '') {
            max_elf_calories.push(current_calories_total);
            current_calories_total = 0;
        } else {
            current_calories_total += Number(element);
        }
    }

    // sort the `max_elf_calories` in reverse order (highest -> lowest)
    max_elf_calories.sort((a, b) => b - a);

    console.log(max_elf_calories.slice(0, 3).reduce((partialSum, a) => partialSum + a, 0));
}

part_1();
part_2();
