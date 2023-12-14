let largest_palidrome: number = 0;
let number: number = 100

while (number < 1000) {
    // loop through all three digit numbers
    for (let second_number = 100; second_number < 1000; second_number++) {
        let current_total: number = number * second_number;
        const current_total_reversed: string = current_total.toString().split("").reduce((acc, char) => char + acc, "");

        // if the product is a palidrome and larger than `largest_palidrome` then update `largest_palidrome`
        if (
            (current_total.toString() == current_total_reversed) &&
            current_total > largest_palidrome
        ) {
            largest_palidrome = current_total
        }
    }
    number += 1;
}

console.log(largest_palidrome);
