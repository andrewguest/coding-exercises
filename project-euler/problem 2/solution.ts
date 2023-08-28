let sum_of_evens: number = 0;
let fibonacci_sequence: number[] = [1, 2];

// Create the Fibonacci sequence for numbers up to 4,000,000
while (Math.max(...fibonacci_sequence) <= 4000000) {
    let next_value: number = fibonacci_sequence[fibonacci_sequence.length -1] + fibonacci_sequence[fibonacci_sequence.length -2];

    if (next_value <= 4000000) {
        fibonacci_sequence.push(next_value);
    } else {
        break;
    }
}

// Sum the even numbers in the Fibonacci sequence from above
for (let index: number = 0; index < fibonacci_sequence.length; index++) {
    const element: number = fibonacci_sequence[index];

    if ((element % 2) == 0) {
        sum_of_evens += element;
    }
}

console.log(sum_of_evens);