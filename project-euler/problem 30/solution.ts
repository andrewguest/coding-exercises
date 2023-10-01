let solution: number = 0;

function sumOfFifthPowers(i: number) {
    const digits = String(i).split('').map(Number);
    const fifthPowers = digits.map(digit => Math.pow(digit, 5));
    const sum = fifthPowers.reduce((acc, val) => acc + val, 0);
    return sum;
}

for (let i = 2; i <= 5 * (9 ** 5) + 1; i++) {
    if (sumOfFifthPowers(i) == i) {
        solution += i;
    }
}

console.log(solution);
