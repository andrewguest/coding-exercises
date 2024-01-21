example_list = [1, 2, 6, 8, 9, 11, 13, 14, 23, 26]
example_n = 15


def find_pairs(input_list: list[int], n: int) -> list|set:
    # Set of numbers from `input_list` that we've already looped over.
    seen_numbers = set()
    result_pairs = set()

    for number in input_list:
        # Subtract the current `number` from `n` and then check if the remaining value is
        #   in `seen_numbers`. If it is then that's a valid pair, otherwise continue through
        #   the list of numbers.
        remaining_value = n - number

        if remaining_value in seen_numbers:
            result_pairs.add((number, remaining_value))

        seen_numbers.add(number)

    return result_pairs


pairs = find_pairs(example_list, example_n)
print(pairs)
