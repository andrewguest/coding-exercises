class Solution:
    def reverse(self, x: int) -> int:

        # Setup for handling negative numbers
        is_negative: bool = str(x).startswith("-")

        # Handle integers larger than 2^31 (2,147,483,647) or less than -2^31 (-2,147,483,647)
        if -2147483647 > x or x > 2147483647:
            return 0

        # Split the number into an array and strip any negative symbols
        digits: list[str] = [n for n in str(x).strip("-")]

        reversed_number = int("".join(digits[::-1]))
        reversed_number *= -1 if is_negative else 1

        # If the reversed value is greater than 2^31 or less than -2^31
        if -2147483647 > reversed_number or reversed_number > 2147483647:
            return 0
        else:
            return reversed_number
