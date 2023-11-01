from random import sample

def randlist(n, a, b):
    """Generates list of random integers of length N.
    Numbers from range [a, b].

    Args:
        n - int, list length.
        a - int, lower limit.
        b - int, upper limit.

    Returns:
        List of integers.
    """

    return sample(range(a, b), n)


if __name__ == "__main__":
    n = int(input("List length N: "))
    a = int(input("Lower limit \'a\': "))
    b = int(input("Upper limit \'b\': "))
    res = randlist(n, a, b)

    print(*res)
