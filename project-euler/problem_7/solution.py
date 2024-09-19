import math


# is_prime function - returns True or False
def is_prime(num):
    # Iterates from 2 to sqrt(num)+1 as discussed above
    # Make sure to convert sqrt to int for range
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


count = 1  # Number of primes
num = 2  # Prime number (count)

# While loop to continue until we reach 100001th prime
while count < 10001:
    num += 1
    if is_prime(num):
        count += 1  # If a prime is found, increase count and continue

# Print answer
print(num)
