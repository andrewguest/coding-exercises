def main():
    a: int = 2
    all_multiples: list[int] = []

    while a < 101:
        for b in range(2, 101):
            all_multiples.append(
                a**b
            )
        a += 1

    print(len(set(all_multiples)))


main()
