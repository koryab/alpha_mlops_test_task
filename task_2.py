from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description='Process some integers.')
    parser.add_argument('points', type=int, nargs='+',
                        help='coordinates of points A, B, C, D respectively.')

    return parser.parse_args()

def count_ratio(points):
    a, b, c, d = points

    return round(abs((a - b)/(c - d)), 6) 

def main():
    args = parse_args()
    print(f"Legths ratio {count_ratio(args)}")

if __name__ == "__main__":
    main()
