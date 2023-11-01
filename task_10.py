import sys

sys.path.insert(0, './alpha_mlops_test_task')

from task_9 import randlist

def sum_positive_7(arr):
    sum = 0
    for n in arr:
        if n % 10 == 7 and n > 0:
            sum += n

    return sum

def main():
    n = int(input("List length N: "))
    a = int(input("Lower limit \'a\': "))
    b = int(input("Upper limit \'b\': "))
    input_data = randlist(n, a, b)
    sum = sum_positive_7(input_data)

    print(sum)


if __name__ == "__main__":
    main()
