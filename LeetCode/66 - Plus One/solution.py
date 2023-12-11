class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # convert the list of integers to a list of strings
        new_digits: list[str] = [str(i) for i in digits]

        # convert the list of string numbers to a single integer
        number: int = int("".join(new_digits))

        # increment by 1
        number += 1

        # convert the integer to a string then convert each back into an integer as part of a list
        answer: list[int] = [int(d) for d in str(number)]

        return answer
