class Solution {
    func reverse(_ x: Int) -> Int {

        // Handle negative numbers
        var is_negative: Bool = String(x).hasPrefix("-")

        // Handle integers greater than or less than 2^31 and -2^31
        if -2147483647 > x || x > 2147483647 {
            return 0
        }

        // Array for all the individual digits of the number
        var digits: Array<String> = []

        for number in String(x) {
            // If the variable is a negative symbol, skip past it
            if number == "-" {
                continue
            } else {
                digits.append(String(number))
            }
        }

        // Reverse the digits array and then join the array into an integer
        digits.reverse()
        var reversed_number: Int = Int(digits.joined(separator: ""))!

        // Make the reversed_number negative if the input number was negative
        if is_negative {
            reversed_number *= -1
        }

        // Handle integers greater than or less than 2^31 and -2^31
        if -2147483647 > reversed_number || reversed_number > 2147483647 {
            return 0
        }

        return reversed_number

    }
}