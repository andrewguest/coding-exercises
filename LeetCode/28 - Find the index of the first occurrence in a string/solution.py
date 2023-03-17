class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # str.find()  -> return the lowest index in the string where substring sub is found within the slice s[start:end].
        return haystack.find(needle)
