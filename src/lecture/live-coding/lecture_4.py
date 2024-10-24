"""
    Return the product of the positive numbers in a list, knowing that one such number exists
"""

data = [-2, -1, 5, 8, -6, -5, 2, -4, -3, 10, 11]  # 8800


# data = [2, 100, 100]


def chip_conquer(data: list) -> int:
    if len(data) == 1:
        if data[0] > 0:
            return data[0]
        else:
            return 1

    p = (data[0] if data[0] > 0 else 1)
    return p * chip_conquer(data[1:])


def divide_conquer(data: list) -> int:
    if len(data) == 1:
        if data[0] > 0:
            return data[0]
        else:
            return 1

    m = len(data) // 2
    return divide_conquer(data[:m]) * divide_conquer(data[m:])


# For O(n) extra memory space calculation, do we regard the call stack space?
def divide_conquer_better(data: list, left: int, right: int) -> int:
    if left == right:
        if data[left] > 0:
            return data[left]
        else:
            return 1

    m = (left + right) // 2
    return divide_conquer_better(data, left, m) * divide_conquer_better(data, m + 1, right)


def divide_conquer_iter(data: list) -> int:
    product = 1

    # Return the product of the positive numbers in a list, knowing that one such number exists
    stack = [(0, len(data) - 1)]

    while len(stack) > 0:
        left, right = stack.pop()

        if left == right:
            if data[left] > 0:
                product *= data[left]
        else:
            m = (left + right) // 2
            stack.append((left, m))
            stack.append((m + 1, right))

    return product


# print(chip_conquer(data))
# print(divide_conquer(data))
# print(divide_conquer_better(data, 0, len(data) - 1))
print(divide_conquer_iter(data))
