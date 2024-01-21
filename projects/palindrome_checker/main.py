example_input = "racecar"


def is_palindrome(input_word: str) -> bool:
    return input_word == "".join(reversed(input_word))


if is_palindrome(example_input):
    print(f"{example_input} is a palindrome")
else:
    print(f"{example_input} is NOT a palindrome")
