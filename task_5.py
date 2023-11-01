from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description="Calculate minimal loader's fee.")
    parser.add_argument("-m", "--height",
                        type=int,
                        required=True,
                        action="store",
                        help=" house height")
    parser.add_argument("-n", "--floor",
                        type=int,
                        required=True,
                        action="store",
                        help=" target floor")
    parser.add_argument("-k",
                        type=int,
                        required=True,
                        action="store",
                        help=" floors available for elevator")

    return parser.parse_args()


def bin_search_upper(x, arr):
    l = 0
    r = len(arr) - 1

    i = 0
    while l + 1 < r:
        m = (r + l) // 2
        if arr[m] == x:
            return arr[m]
        elif arr[m] > x:
            r = m
        else:
            l = m
        i += 1

    return arr[r]


def count_fee(m, n, k):
    UP = 200
    DOWN = 100

    k_floors = list(range(1, m, k))
    k_upper = bin_search_upper(n, k_floors)
    fee = min([abs(n - k_upper - k) * UP, (k_upper - n) * DOWN])

    return fee


def main():
    args = parse_args()
    m = args.height
    n = args.floor
    k = args.k

    print(count_fee(m, n, k))


if __name__ == "__main__":
    main()