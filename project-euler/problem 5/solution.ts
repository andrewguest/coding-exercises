function gcd_rec(a, b) {
    if (b) {
        return gcd_rec(b, a % b);
    } else {
        return Math.abs(a);
    }
}


function main() {
    let answer: number = 1;

    for (let i = 1; i < 21; i++) {
        answer *= Math.floor(
            i / (gcd_rec(i, answer))
        )
    }

    console.log(answer);
}


main();
