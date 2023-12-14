var answer: Int = 1

// Function to find gcd of two numbers
func findGCD(num1: Int, num2: Int) -> Int {
    var x = 0

    // Finding maximum number
    var y: Int = max(num1, num2)

    // Finding minimum number
    var z: Int = min(num1, num2)

    while z != 0 {
        x = y
        y = z
        z = x % y
    }

    return y
}


for i in 1...20 {
    answer *= i / findGCD(i, answer)
}

print(answer)
