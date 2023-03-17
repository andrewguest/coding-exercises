class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s.split()  -> split "s" into an array of string by removing all spaces
        # [-1]  -> last element in array
        return len(s.split()[-1])
