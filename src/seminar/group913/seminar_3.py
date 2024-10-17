"""
    Determine the time complexity of the following algorithms as a function of n.
    sources:
        https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
        https://www.geeksforgeeks.org/practice-questions-time-complexity-analysis/
"""
from random import random

"""
    Time complexity notation:
        n - size of the algorithm's input (length of the list, number of elements of a matrix, an index)
        T(n) - function that represents the number of operations carried out by the algorithm for input size n
        # T(n) = 2 * n leads to linear time
        
        after we calculate/approximate T(n) we can talk about the time complexity
        Going from T(n) to time complexity:
            1. Only consider the dominating term (when n grows large)
            2. Throw out any constants
        Algorithm complexity:
            BigO => O(n) -> high bound on algorithm complexity (algorithm cannot be slower than this)
            BigOmega => Omega(n) -> low bound on algorithm complexity (algorithm cannot be faster than this)
            Theta => Theta(n) -> the exact complexity (both low and high bound), not sure this exists!?
    Extra-space complexity
        - how much additional memory space the algorithm requires to do its job
        - we do not consider the input
        
    Notes:
        -> Every operation that does not depend on "n" takes 1 unit of time
        -> Function allocates a quantity of memory that does not depend on "n" -> 1 unit of space :) 
"""


def f_1(n: int):
    for i in range(10):
        for j in range(n):
            print("Hello World")


def f_2(n: int):
    for i in range(n, n + 10):
        for j in range(n):
            print("Hello World")


def f_3(n: int):
    for i in range(1, n):
        for j in range(i, n):
            print("Hello World")


def f_4(n: int):
    for i in range(n):
        for j in range(2 * i + 1):
            print("Hello World")


def f_5(n: int):
    for i in range(n ** 2):
        for j in range(i):
            print("Hello World")


def f_6(n: int):
    for i in range(n):  # n
        t = 1
        while t < n:
            print("Hello World")
            t *= 2


"""
    Time complexity depends on both "n" and "m"
"""


def f_7(n, m: int):
    for i in range(0, n):  # n loops
        print("Hello World")
    for j in range(0, m):  # m loops
        print("Hello World")


def f_8(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, n):
        print("Hello World")


def f_9(n: int):
    for i in range(n):
        for j in range(n):
            print("Hello World")
        for k in range(n):
            print("Hello World")


def f_10(n: int):
    for i in range(n):
        for j in range(n, i, -1):
            print("Hello World")


def f_11(n: int, m: int) -> None:
    a = 0
    b = 0
    for i in range(n):
        a = a + random()

    for i in range(m):
        b = b + random()


def f_12(n: int) -> None:
    k = 0
    for i in range(n // 2, n):
        for j in range(2, n, pow(2, j)):
            k = k + n / 2


"""
    Analyze the time and space complexity 
"""


def f_13(data: list) -> int:
    data_sum = 0
    for el in data:
        j = len(data)
        while j > 1:
            data_sum += el * j
            j = j // 3
    return data_sum


def f_14(data: list) -> int:
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_14(data[:m]) + f_14(data[m:])


def f_15(n: int) -> int:
    s = 0
    for i in range(1, n ** 2):
        j = i
        while j != 0:
            s = s + j - 10 * j // 10
            j //= 10
    return s


def f_16(n, i: int) -> None:
    if n > 1:
        i *= 2
        m = n // 2
        f_16(m, i - 2)
        f_16(m, i - 1)
        f_16(m, i + 2)
        f_16(m, i + 1)
    else:
        print(i)


"""
Analyze the algorithm's time complexity. Write an equivalent algorithm with 
a strictly better time complexity
"""


def f_17(data: list) -> int:
    i = 0
    j = 0
    m = 0
    c = 0
    while i < len(data):
        if data[i] == data[j]:
            c += 1
        j += 1
        if j >= len(data):
            if c > m:
                m = c
            c = 0
            i += 1
            j = i
    return m


"""
    What is the time complexity when implementing the following algorithm. How can this be 
    optimized and how will that improve the complexity?
"""


def f_18(x, n: int):
    """
    The algorithm returns x ** n
    :param x:
    :param n:
    :return:
    """
    # TODO Implement me
    pass
