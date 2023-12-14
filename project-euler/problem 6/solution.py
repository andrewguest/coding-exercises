sum_of_squares: int = sum(list(map(lambda x: x**2, range(1, 101))))
square_of_sums: int = sum(range(1, 101)) ** 2

print(square_of_sums - sum_of_squares)
