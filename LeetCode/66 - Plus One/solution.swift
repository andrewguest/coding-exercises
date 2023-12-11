class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        // string list version of the digits array
        var new_digits: [String] = []

        // integer version of the new number
        var number: Int

        // integer list version of the new number
        var answer: [Int] = []

        for i: Int in digits {
            new_digits.append(String(i))
        }

        // convert the string list from above to an integer value incremented by 1
        number = Int(new_digits.joined(separator: ""))! + 1



    }
}