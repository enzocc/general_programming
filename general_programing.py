import argparse


def fibo_even_100():
    """
    Write a program in a language of your choice to calculate the
    sum of the first 100 even-valued Fibonacci numbers
    """
    res = []
    fibo_n_1 = 1
    fibo_n_2 = 1

    while len(res) < 100:
        fibo_n = fibo_n_1 + fibo_n_2
        fibo_n_2 = fibo_n_1
        fibo_n_1 = fibo_n
        if not (fibo_n % 2):
            res.append(fibo_n)
    return sum(res)


def two_sorted_arrays(a1, a2):
    """
    Write a function in a language of your choice which, when passed
    two sorted arrays of integers returns an array of any numbers
    which appear in both. No value should appear in the returned
    array more than once.
    """
    set_a1 = set(a1)
    set_a2 = set(a2)
    return set_a1.intersection(set_a2)


def no_odd_digits(num):
    """
    Write a function in a language of your choice which, when
    passed a positive integer returns true if the decimal
    representation of that integer contains no odd digits
    and otherwise returns false.
    """
    if num < 0 or type(num) is not int:
        return False
    string_num = str(num)
    for dd in string_num:
        if int(dd) % 2 == 1:
            return False
    return True


def digit_sum(num):
    """
    Write a function in a language of your choice which, when
    passed a decimal digit X, returns the value of X+XX+XXX+XXXX.
    E.g. if the supplied digit is 3 it should return 3702
    (3+33+333+3333).
    """
    if num < 0 or num > 9:
        return 0
    return num * (1 + 11 + 111 + 1111)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inputq3",
        help="This is the positive integer to test in Question #3."
    )
    parser.add_argument(
        "--inputq4",
        help="This is the digit used in Question #4"
    )
    args = parser.parse_args()
    inputq3 = int(args.inputq3)
    inputq4 = int(args.inputq4)

    if not inputq3:
        raise Exception("No positive integer provided. Use flag '--inputq3'")

    if not inputq4:
        raise Exception("No digit provided. Use flag '--inputq4'")

    print("Answer 1: {}".format(fibo_even_100()))
    # print("Answer 2: ".format(two_sorted_arrays()))
    print("Answer 3: {}".format(no_odd_digits(inputq3)))
    print("Answer 4: {}".format(digit_sum(inputq4)))
