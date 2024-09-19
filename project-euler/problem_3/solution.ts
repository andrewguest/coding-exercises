function prime_factor(number:number) {
    let largest_factor = 1;
    let c = number;
    let i = 2;

    while (c > 1) {
        if ((c % i) == 0) {
            largest_factor = i;
            c = Math.floor(c / i);
        }
        i += 1;
    }

    console.log(largest_factor);
}

prime_factor(600851475143);