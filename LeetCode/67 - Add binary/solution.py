class Solution:
    def add_binary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
