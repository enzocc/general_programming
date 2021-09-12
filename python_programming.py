def calc_sum(num1, num2):
    """
    Define a generator which generates the positive integers
    up to and including a supplied value which are divisible
    by another supplied positive integer and use it to
    calculate the sum of all positive integers less than
    102030 which are divisible by 3
    """
    def my_generator(num1, num2):
        nn = num2
        while nn <= num1:
            yield nn
            nn += num2
    res = 0
    for nn in my_generator(num1, num2):
        res += nn
    return res


def create_lists(num):
    """
    Write a function which is passed an integer, n, and returns
    a list of n lists such that:
    f(0) returns []
    f(1) returns [[1]]
    f(2) returns [[1], [1,2]]
    f(3) returns [[1], [1,2], [1,2,3]]
    etc.
    """
    res = []
    if num == 0:
        return res

    for i in range(1, num+1):
        res.append(list(range(1,i+1)))
    return res