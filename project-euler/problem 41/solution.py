from itertools import permutations

p = permutations("1234567")
largest_pandigital_prime = 0


def is_prime(n) -> bool:
    """Function to check if
    the given number is prime"""
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


for i in list(p)[::-1]:
    if int(i[6]) % 2 != 0:
        number = int("".join(i))
        if (number+1) % 6 == 0 or (number-1) % 6 == 0:
            if is_prime(number):
                print(number)
                break
