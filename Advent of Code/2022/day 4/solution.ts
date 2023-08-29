import * as fs from "fs";


function read_file_lines(file_name: string = "./input.txt"): string[] {
    const input = fs.readFileSync(file_name, "utf-8");
    const input_array = input.split("\n");

    return input_array;
}


function day_1() {
    let file_lines = read_file_lines();
    let fully_contained_pairs = 0;

    for (let index = 0; index < file_lines.length; index++) {
        const line = file_lines[index];
        let first: any = line.split(",")[0];
        let first_array: Number[] = [];
        let first_start = first.split("-")[0];
        let first_end = first.split("-")[1];

        let second: any = line.split(",")[1];
        let second_array: Number[] = [];
        let second_start = second.split("-")[0];
        let second_end = second.split("-")[1];

        if (first_start != first_end) {
            for (let index = Number(first_start); index <= Number(first_end); index++) {
                first_array.push(Number(index));
            }
        } else {
            first_array = [Number(first_start)];
        }

        if (second_start != second_end) {
            for (let index = Number(second_start); index <= Number(second_end); index++) {
                second_array.push(Number(index));
            }
        } else {
            second_array = [Number(second_start)];
        }

        if (first_array == second_array) {
            fully_contained_pairs += 1;
        } else if (first_array.every(element => second_array.includes(element))) {
            fully_contained_pairs += 1;
        } else if (second_array.every(element => first_array.includes(element))) {
            fully_contained_pairs += 1;
        }

    }

    console.log(fully_contained_pairs);
}


day_1();
