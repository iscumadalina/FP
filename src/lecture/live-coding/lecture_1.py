"""
Problem statement:
    1. Read a string from the program's console
    2. Divide the string into numbers, words (using space)
    3. Build a list of primes, a list of negative numbers, a list of the rest of the numbers, a list
    of capitalized names

    4. Print out all primes numbers etc. in ascending order, without duplicates :)
"""
from math import sqrt


def is_capitalized(word: str) -> bool:
    return 'A' <= word[0] <= 'Z'


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # range -> start with 3 then +2 at every step until sqrt(n) + 1
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


# 45 -14 23 -5 Anna has apples 55 -50 23 -5 James 47 999
line = input("Give the string =")
# print(type(line))  # print the type of the line variable

# print(line)
tokens = line.split(" ")

primes_list = []  # empty list
negatives_list = []
other_numbers_list = []
cap_names_list = []

# negatives_list = "s"

for token in tokens:
    try:
        int_token = int(token)  # int() is a builtin function to convert to integer
        # if there's an error on the previous line, the execution skips directly
        # to the except clause below
        if int_token < 0:
            negatives_list.append(int_token)
        elif is_prime(int_token):
            primes_list.append(int_token)
        else:
            other_numbers_list.append(int_token)
    except ValueError:
        if is_capitalized(token):
            cap_names_list.append(token)

# TODO Do the same as below for the remaining lists
primes_list = list(set(primes_list))
primes_list.sort()

# negatives_list.sort()
#
print(primes_list)
# print(negatives_list)  # converting the list into a set will eliminate the duplicates
# print(other_numbers_list)
# print(cap_names_list)
