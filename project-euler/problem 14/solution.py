from tqdm import tqdm


class CollatzCache:
    def __init__(self) -> None:
        self._cache = {}

    def compute_length(self, start: int) -> int:
        steps = 0
        number = start
        while number != 1:
            if number in self._cache:
                self._cache[start] = self._cache[number] + steps
                return self._cache[number] + steps

            if number % 2 == 0:
                number //= 2
            else:
                number = 3 * number + 1
            steps += 1

        self._cache[start] = steps

        return steps


def solution_cached() -> int:
    collatz_cache = CollatzCache()
    result = 0
    max_steps = 0
    for start in tqdm(range(1, 1_000_000)):
        steps = collatz_cache.compute_length(start)
        if steps > max_steps:
            max_steps = steps
            result = start

    return result


print(solution_cached())
