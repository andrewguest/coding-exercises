max_number = 1_000_000
total = 0

def is_palindrome_base_10(number: int) -> bool:
    """Check if the given number is a palindrome in base 10"""
    if str(number).startswith("0"):
        return False
    else:
        return str(number) == str(number)[::-1]


def is_palindrome_base_2(number) -> bool:
    """Check if the given number is a palindrome in base 2"""
    number = bin(number).replace("0b", "")
    if str(number).startswith("0"):
        return False
    else:
        return str(number) == str(number)[::-1]


for n in range(1, max_number):
    if is_palindrome_base_10(n) and is_palindrome_base_2(n):
        total += n


print(total)
