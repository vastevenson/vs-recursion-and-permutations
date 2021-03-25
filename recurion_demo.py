'''
Goal: define a method that takes an integer and returns the factorial of that integer using recursion.

Assume n is a positive integer.

Ex: 4! = 4*3*2*1
4! = 4*(3!) [recursive case]
3! = 3*(2!) [recursive case]
2! = 2*(1!) [recursive case]
1! = 1*(0!) [recursive case]
0! = 1 [base case]
'''

def fac(n):
    # base case
    if n == 0:
        return 1
    # recursive case
    else:
        return n*fac(n-1)

# print(fac(4))


'''
Fibonacci sequence: 1,1,2,3,5,8,13,21,34
Base case: 
n = 1 or n = 2, then fib(n) == 1
Recursive case: 
fib(3) = fib(2) + fib(1) 
fib(n) = fib(n-1) + fib(n-2)
'''

def fib(n):
    if n == 1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(4)) # expect 3