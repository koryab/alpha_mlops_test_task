from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description="Executes lenghts of segments AB to CD ratio.")
    parser.add_argument("-c", "--coords",
                        nargs="+",
                        required=True,
                        action="store",
                        help="coordinates of points A, B, C, D respectively.")

    return parser.parse_args()

def count_ratio(coords):
    a, b, c, d = list(map(float, coords))

    return round(abs((a - b)/(c - d)), 6) 

def main():
    args = parse_args()
    coords = args.coords
    print(f"Legths ratio {count_ratio(coords):.6}")

if __name__ == "__main__":
    main()
