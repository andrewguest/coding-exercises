class Solution {
    func lengthOfLastWord(_ s: String) -> Int {
        // split the "s" string by spaces into an array of Substrings
        var substring_array: [Substring] = s.split(separator: " ")

        // get the last Substring from the substring_array array above and explicitly convert it to a Substring
        var last_word: Substring = substring_array.last!

        // return the count of characters in the "last_word" Substring
        return last_word.count
    }
}