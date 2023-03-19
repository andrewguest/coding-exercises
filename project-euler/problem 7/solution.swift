func isPrime(num: Int) -> Bool {
    for i: Int in 2...Int(Double(num).squareRoot() + 1) {
        if num % i == 0 {
            return false
        }
    }
    return true
}


var count: Int = 1  // Count of prime numbers found
var num_to_check: Int = 2  // Number to check

while count < 10001 {
    num_to_check += 1

    if isPrime(num: num_to_check) {
        count += 1
    }
}

print("The 10,001st prime is: \(num_to_check)")
