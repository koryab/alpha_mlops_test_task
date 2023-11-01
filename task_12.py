import sys

sys.path.insert(0, './alpha_mlops_test_task')

from task_9 import randlist

def biggest_even(arr):
    max_even = 0
    for n in arr:
        if not (n % 2) and n > max_even:
            max_even = n

    return max_even

def main():
    n = int(input("List length N: "))
    a = int(input("Lower limit \'a\': "))
    b = int(input("Upper limit \'b\': "))
    input_data = randlist(n, a, b)
    sum = biggest_even(input_data)

    print(sum)

if __name__ == "__main__":
    main()
