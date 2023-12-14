// reverse the order of digits in the given integer
func reverse_number(number: Int) -> Int {
    var reverseNum = 0
    var digit: Int = number

    while(digit != 0) {
        reverseNum = reverseNum * 10
        reverseNum = reverseNum + digit % 10
        digit = digit/10
    }

    return reverseNum

}


var largest_palidrome: Int = 0
var num: Int = 100

// loop through all three digit numbers for the first number in the multiplication formula
// num * second_number = current_total
while num < 1000 {
    // loop through all three digit numbers for the second number in the multiplication formula
    for second_number: Int in 100...999 {
        let current_total: Int = num * second_number
        let reversed_current_total: Int = reverse_number(number: current_total)

        // if the current_total is a palidrome and greater than largest_palidrome then update largest_palidrome
        if (current_total == reversed_current_total) && current_total > largest_palidrome {
            largest_palidrome = current_total
        }
    }

    // increase num by 1 and start the loop over again for second_number (starting at 100 and going up to 999)
    num += 1
}

print(largest_palidrome)
