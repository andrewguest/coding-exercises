import * as fs from "fs";


function read_file_lines(file_name: string = "./input.txt"): string[] {
    const input = fs.readFileSync(file_name, "utf-8");
    const input_array = input.split("\n");

    return input_array;
}


function part_1(): number {
    const data: string[] = read_file_lines();

    let t: number = 0;

    for (const line of data) {
        const [a, b, c, d]: number[] = line.match(/(\d+)/g)!.map(Number);

        if ((a >= c && b <= d) || (c >= a && d <= b)) {
            t += 1;
        }
    }

    return t;
}


function part_2(): number {
    const data: string[] = read_file_lines();

    let t: number = 0;

    for (const line of data) {
        const [a, b, c, d]: number[] = line.match(/(\d+)/g)!.map(Number);

        if ((b >= c && b <= d) || (d >= a && d <= b)) {
            t += 1;
        }
    }

    return t;
}


console.log(`Part 1: ${part_1()}`);
console.log(`Part 2: ${part_2()}`)
