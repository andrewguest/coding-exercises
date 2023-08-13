def prime_factor(number):
    largest_factor = 1
    c = number
    i = 2

    while c > 1:
        if c % i == 0:
            largest_factor = i
            c = c // i
        i += 1
    print(largest_factor)


prime_factor(600851475143)
