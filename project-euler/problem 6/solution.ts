let sum_of_squares: number = 0;
let square_of_sums: number = 0;

for (let i = 1; i <= 100; i++) {
    sum_of_squares += i ** 2;
    square_of_sums += i;
}

console.log((square_of_sums ** 2) - sum_of_squares);