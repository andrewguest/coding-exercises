var total: number = 0;

for (var i: number = 1; i < 1000; i++) {
    if (((i % 3) == 0) || ((i % 5) == 0)) {
        total += i;
    }
}

console.log(total);