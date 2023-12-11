class Solution {
    func isPalindrome(_ x: Int) -> Bool {

        // convert "x" to a String and compare it to a reversed String version of "x"
        return String(x) == String(String(x).reversed())
    }
}