from random import randint
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description="Analyse 2000-digits number from file")
    parser.add_argument("-f", "--file",
                        type=str,
                        default="task_7_output.txt",
                        action="store",
                        help=" path to output file")

    return parser.parse_args()


def most_frequent(number):  
    distribution = {str(d): 0 for d in range(0, 10)}
    max_freq = 0, 0
    for digit in number:
        distribution[digit] +=  1
        if int(distribution[digit]) > max_freq[1]:
            max_freq = digit, distribution[digit]

    return max_freq


def is_even(number):
    return not bool(int(number[-1]) % 2 )


def main():
    file = parse_args().file
    
    with open(file, "r") as f:
        number = f.read()
    
    digit, frequency = most_frequent(number)
    print("Most frequent digit in the number "
          f"is {digit}, appears {frequency}.")
    
    if  is_even(number):
        print("The number is even.")
    else:
        print("The number is odd.")


if __name__ == "__main__":
    main()
