let prime_numbers: number[] = [];  // list of prime numbers
let number: number = 2;  // starting number

function isPrime(n: number): boolean {
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

while (number < 2000000) {
    if (isPrime(number)) {
        prime_numbers.push(number);
    }

    number += 1;
}

console.log(prime_numbers.reduce((partialSum, a) => partialSum + a, 0));
