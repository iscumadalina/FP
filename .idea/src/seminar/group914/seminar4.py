"""
    Problem Solving Methods -- Divide & Conquer, Backtracking
"""

"""
    1. Implement an optimized version of the merge sort algorithm
        a. Implement Merge Sort
        b. Use the insertion sorting algorithm with the binary search optimization found in the lecture examples
        c. Time the resulting version using the ex17_sort_comparison.py example
        d. Discuss how merging might be improved using exponential search
"""

from random import shuffle, randint

def binary_search(arr, val, start, end):
    # we need to distinguish whether we should insert before or after the left boundary. imagine [0] is the last
    # step of the binary search and we need to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    # this occurs if we are moving beyond left's boundary meaning the left boundary is the least position to find a
    # number greater than val
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def binary_insertion_sort(data: list):
    for i in range(1, len(data)):
        val = data[i]
        j = binary_search(data, val, 0, i - 1)
        # This is O(n) space complexity, but it can be simplified by moving elements one by one
        data = data[:j] + [val] + data[j:i] + data[i + 1:]
    return data

def gen_list(n):
    # result = []
    data = []
    while(n > 0):
        data.append(randint(0, 200))
        n -= 1
    # shuffle(data)
    return data

def merge(list_one, list_two):
    result = []
    index_one = 0
    index_two = 0
    
    while index_one < len(list_one) and index_two < len(list_two):
        if list_one[index_one] < list_two[index_two]:
            result.append(list_one[index_one])
            index_one += 1
        else:
            result.append(list_two[index_two])
            index_two += 1
            
    while index_one < len(list_one):
        result.append(list_one[index_one])
        index_one += 1
        
    while index_two < len(list_two):
        result.append(list_two[index_two])
        index_two += 1
        
    return result

"""
def merge_sort(data: list):
    # base case of the recursion - T(n) = 1
    if len(data) == 1:
        return data
    m = len(data) // 2
    left_half = merge_sort(data[:m])  # index m is excluded, just like the right parameter in range()
    right_half = merge_sort(data[m:])  # data[:] creates a copy of the list
    
    # merge into the original list
    return merge(left_half, right_half)
    
"""
    
def merge_sort(data: list):
    # base case of the recursion - T(n) = 1
    if len(data) == 1:
        return data
    elif len(data) < 16:
        return binary_insertion_sort(data)

data = [x for x in range(20, 0, -1)]
res = merge_sort(data)
# data = list(range (20, 0, -1))
# ata.sort(reverse = True)  # reverse is a keyword argument
# print(data)
# print(res) 

# x = gen_list(10)
# print(list)

def test_sort():
    for i in range(1000):
        data = gen_list(randint(1, 500))
        sorted_py = sorted(data)
        sorted_merge = merge_sort(data)
        
        # assert crashes the program is the expression is False
        assert sorted_py == sorted_merge
        
test_sort()
   
"""
    2. Find the smallest number in a list using a recursive divide & conquer implementation. Return None for an empty 
    list. Implement the following variants:
        a. Chip & conquer
        b. Divide the list into halves
"""

"""
    3. Calculate the r-th root of a given number x with a given precision p
    
    e.g. calculate the 12th root of 3 with precision 0.0001
    x = 3
    r = 12
    p = 0.0001
    (radical de ordin 12 din 3)
    
    v at the power of 12 is aproximatly equal with 3
    3 - p < v < 3 + p
    
"""

calls = 0
    
def rth_root(x, root, p, left, right) -> float: # iordachioaiei alex
    global calls  # refer to the global variable calls
    calls += 1
    mid = (left + right)/2
    power = mid ** root

    if x - p <= power <= x + p:
        return mid
    if x >= 1:
        if mid ** root < x + p:
            return rth_root(x, root, p, mid, right)
        else:
            return rth_root(x, root, p, left, mid)  
    else:
        if mid ** root < x + p:
            return rth_root(x, root, p, left, mid)
        else:
            return rth_root(x, root, p, mid, right)
    
def calc_root(x, root, p):
    """
    Return a value v, so that x - p < v^r < x + p
    - param x: the number we extract root from
    - param r: the order of the root
    - param p: the precision required
    - return: a value v, so that x - p < v^r < x + p
    
    """
    return rth_root(x, root, p, 1, x)

# v = calc_root(3, 12, 0.0001)
v = calc_root(8.5, 10, 0.0000001)
print(v, v ** 10)
print(calls)
        
"""
    4. Calculate the maximum subarray sum (elements of a subarray have consecutive indices in the parent array)
        a. Naive implementation
        b. Divide & conquer implementation
        c. Dynamic programming implementation (next week)

        e.g.
        for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""

"""
    5. All permutations of the {0, 2, ..., n - 1} set (recursive implementation)
"""


def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """
    return len(set(x)) == len(x)


def solution(x, n):
    """
    Determines whether we have a solution
    """
    return len(x) == n


def solution_found(x):
    """
    What to do when a solution is found
    """
    print("Solution: ", x)


def bkt_rec(x, n):
    """
    Backtracking algorithm for permutations problem, recursive implementation
    """
    x.append(0)
    for i in range(0, n):
        x[len(x) - 1] = i
        if consistent(x):
            if solution(x, n):
                solution_found(x)
            else:
                bkt_rec(x[:], n)


# bkt_rec([], 4)

"""
    6. Change the code above to work for the n-Queen problem
"""

"""
    7. A Latin square is an n × n square filled with n different symbols, each occurring exactly once in each row and 
    exactly once in each column

    Generate all the N x N Latin squares for a given number N. 
"""

"""
    8. Generate all reduced N x N Latin squares for a given number N. In a reduced Latin square, the elements of the 
    first row and first column are sorted.
"""
