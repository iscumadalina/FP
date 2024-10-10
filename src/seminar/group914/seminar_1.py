"""
FP seminar 1 problems & solutions
"""

"""
Problem statements to choose from:
    https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
    https://www.freecodecamp.org/news/python-coding-challenges-for-beginners/
"""

"""
1. Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10
Question – What happens if we enter a non-integer number, or alphanumeric characters?

str type - concatenation
int type - addition

"""

"""
2. Write a Python program which iterates the integers from 1 to 50. 
For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".

# V1 - without functions
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# V2 - using functions
def fizz_buzz(left: int, right: int) -> list:
    result = [] # empty list
    for i in range(left, right + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

print(fizz_buzz(0, 16))

"""

"""
3. Calculate the first n terms of the Fibonacci sequence

n = int(input("n = "))
a = b = 1
n -= 2
print(1)
print(1)
while n != 0:
    c = a + b
    print(c)
    a = b
    b = c
    n -= 1

"""

"""
4. Write a Python program to calculate body mass index.
   How do we validate the code above for user input?
   Let's write the specification for it

   
def BMI(weight, height):
    return weight / (height * height)

weight = float(input("weight = "))
height = float(input("height = ")) 
bmi = BMI(weight, height)
if bmi <= 18.4:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal")
elif bmi >= 25 and bmi <= 39.9:
    print("Overweight")
else:
    print("Obse")

"""

"""
5. Given a non-empty string like "Code" return a string like "CCoCodCode"
    string_splosion('Code') → 'CCoCodCode'
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'
"""

"""
6. Given 2 strings, a and b, return the number of the positions where they contain the same length 2
substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the
same place in both strings.
    stringMatch('xxcaazz', 'xxbaaz') → 3
    stringMatch('abc','abc) → 2
        stringMatch('abc', 'axc') → 0
"""

"""
7. Write a Python program to remove all duplicate elements from a given array and returns a new array.
"""

"""
8. Return the sum of the numbers in a list, returning 0 for an empty list. Except the number 13 is very
unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
"""

"""
9. Caesar Encryption
"""
