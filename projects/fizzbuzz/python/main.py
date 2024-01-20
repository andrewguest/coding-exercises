for number in range(1, 101):
    # multiples of 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # multiples of 3
    elif number % 3 == 0:
        print("Fizz")
    # multiples of 5
    elif number % 5 == 0:
        print("Buzz")
    # all other numbers
    else:
        print(number)
