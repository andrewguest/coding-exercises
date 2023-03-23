var number_of_test_cases: String = readLine()!

for _ in 1...Int(number_of_test_cases)! {
    var dice_rolls: String = readLine()!
    var dice_digits: [Int] = dice_rolls.split(separator: " ")

    if (dice_digits[0] + dice_digits[1]) > 6 {
        print("YES")
    } else {
        print("NO")
    }
}