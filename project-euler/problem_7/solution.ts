let counter = 2;
const primeNumbers: number[] = [];
const end = 10001;

function isPrime(n: number): boolean {
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

while (primeNumbers.length < end) {
    if (counter > 2 && counter % 2 === 0) {
        counter++;
        continue;
    }

    if (isPrime(counter)) {
        primeNumbers.push(counter);
    }

    counter++;
}

console.log(primeNumbers[end - 1]);