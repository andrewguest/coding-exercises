class Solution:
    def isPalindrome(self, x: int) -> bool:

        # convert "x" to a string, reverse it and compare it to the original string
        #   version of "x"
        return str(x) == str(x)[::-1]
