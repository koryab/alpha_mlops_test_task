from random import randint
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description="Generates random 2000-digits number into file")
    parser.add_argument("-f", "--file",
                        type=str,
                        default="task_7_output.txt",
                        action="store",
                        help=" path to output file")

    return parser.parse_args()


def generate_number(file):  
    with open(file, "w") as out:
        set_digit = lambda x: print(x, end="", file=out)
        set_digit(randint(1, 9))    
        for i in range(1, 2000):
            set_digit(randint(0, 9))

    print(f"Number saved to \"{file}\".")


def main():
    file = parse_args().file
    generate_number(file)


if __name__ == "__main__":
    main()