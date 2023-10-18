import Foundation


func prime_factor(number: Int) {
    var largest_factor: Int = 1
    var c: Int = number
    var i: Int = 2

    while c > 1 {
        if (c % i == 0) {
            largest_factor = i
            c = Int(floor(Double(c / i)))
        }

        i += 1
    }

    print(largest_factor)
}

prime_factor(number: 600851475143)