import math

prime_numbers: list[int] = []
number = 2


def is_prime(num):
    # Iterates from 2 to sqrt(num)+1 as discussed above
    # Make sure to convert sqrt to int for range
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


while number < 2000000:
    if is_prime(number):
        prime_numbers.append(number)

    number += 1


print(sum(prime_numbers))
