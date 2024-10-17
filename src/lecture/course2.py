""" #  FACTORIAL

def fact(n):
    # Base case of recursion
    if n == 0:
        return 1
    
    # Recursion progresses towards the base case
    return n * fact(n - 1)

for i in range(25):
    # fact(i)  # overflow
    print(i, fact(i))
    
"""  #  FIBONACCI
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)

# cache or memorization
cache = { 0 : 1 , 1 : 1 }  # key 0 has associated value 1, key 1 has associated value 1
def fib_cached(n):
    if n in cache:
        return  cache[n]
    return fib_cached(n - 2) + fib_cached(n - 1)
    return cache[n]

for i in range(1, 30):
    print(i, fib(i))
    
 