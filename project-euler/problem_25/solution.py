def main():
    fibonacci_sequence: list[int] = [1, 1]


    while ( len(str(fibonacci_sequence[-1])) != 1000 ):
        fibonacci_sequence.append(
            fibonacci_sequence[-1] + fibonacci_sequence[-2]
        )

    print(len(fibonacci_sequence))


main()
