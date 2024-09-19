const LIMIT = 500;
let product!: number;

for (let i = 3; i <= LIMIT; i++) {
    for (let j = i + 1; j <= LIMIT; j++) {
        const k = Math.sqrt(i ** 2 + j ** 2);
        if (i + j + k === 1000) {
            product = i * j * k;
        }
    }
}

console.log(product);

