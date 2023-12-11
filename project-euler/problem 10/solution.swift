var prime_numbers: [Int] = []
var number: Int = 2


func isPrime(num: Int) -> Bool {
    for i: Int in 2...Int(Double(num).squareRoot() + 1) {
        if num % i == 0 {
            return false
        }
    }

    return true
}


while number < 2000000 {
    if isPrime(num: number) {
        prime_numbers.append(number)
    }

    number += 1
}


print(prime_numbers.reduce(0, +))
