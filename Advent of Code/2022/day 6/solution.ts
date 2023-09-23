import * as fs from "fs";


function read_file_lines(file_name: string = "./input.txt"): string[] {
    const input = fs.readFileSync(file_name, "utf-8");
    const input_array = input.split("\n");

    return input_array;
}


function part_1(): number {
    const data: string = read_file_lines()[0];
    let packet_start_index = 0;
    let start_index: number = 0;
    let end_index: number = 4;

    while (packet_start_index == 0) {
        let current_substring: string = data.substring(start_index, end_index);
        let current_substring_as_array: string[] = [...current_substring];
        let current_substring_as_set = new Set(current_substring_as_array);

        if (current_substring_as_array.length == Array.from(current_substring_as_set).length) {
            packet_start_index = end_index;
            break;
        } else {
            start_index += 1;
            end_index += 1;
        }
    }

    return packet_start_index;
}


function part_2(): number {
    const data: string = read_file_lines()[0];
    let message_start_index = 0;
    let start_index: number = 0;
    let end_index: number = 14;

    while (message_start_index == 0) {
        let current_substring: string = data.substring(start_index, end_index);
        let current_substring_as_array: string[] = [...current_substring];
        let current_substring_as_set = new Set(current_substring_as_array);

        if (current_substring_as_array.length == Array.from(current_substring_as_set).length) {
            message_start_index = end_index;
            break;
        } else {
            start_index += 1;
            end_index += 1;
        }
    }

    return message_start_index;
}


console.log(`Part 1: ${part_1()}`);
console.log(`Part 2: ${part_2()}`);
