from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description="Process some integers.")
    parser.add_argument("-d", "--days",
                        type=int,
                        required=True,
                        action="store",
                        help=" number of days passed")

    return parser.parse_args()

def weeks_passed(days):
    return days // 7

def main():
    days = parse_args().days
    print(weeks_passed(days))

if __name__ == "__main__":
    main()