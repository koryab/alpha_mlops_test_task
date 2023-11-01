from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description="Counts amoebas quantity after N hours.")
    parser.add_argument("-n", "--hours",
                        type=int,
                        required=True,
                        action="store",
                        help=" number of hours passed")

    return parser.parse_args()

def main():
    hours = parse_args().hours
    if (hours % 3) or hours > 90:
        exit("Incorrect N, must be 3 <= N <= 90 and multiple of 3.")
    
    print(2 ** (hours // 3))

if __name__ == "__main__":
    main()