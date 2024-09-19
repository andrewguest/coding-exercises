from math import factorial


def nck(n, k):
    """Calculate the binomial coefficient

    Args:
        n (int):
        k (int):

    Returns:
        int
    """
    return factorial(n) / (factorial(k) * factorial(n-k))


print(int(nck(40, 20)))
