##Implement function factorial() that takes as input a nonnegative integer
##and returns its factorial.

##The factorial of a nonnegative integer n, denoted n!, is defined in this way:
##n! = 1 if n = 0
##n! = n* (n-1) * (n-2) * ... * 2 * 1 if n > 0
## (Perkovic 136)

def factorial(num):
    'Takes as input a nonnegative integer and returns the factorial value'
    if num == 0:
        return 1
    
    elif num > 0:

        total = 1
        for n in range(1, num +1):
            total *= n
        print(total)

