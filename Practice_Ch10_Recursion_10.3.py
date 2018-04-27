##In Chapter 5, we implemented function factorial() iteratively.
##
##The factorial function n! has a natural recursive definition:
##n! =	1 if n = 0
##n·(n−1)! if n > 0
##Reimplement function factorial() function using recursion.
##Also, estimate how many calls to factorial() are made for
##some input value n > 0.
## (Perkovic 334)

def factorial(n):
    'Returns factorial of given integer'

    if n == 0:

        return 1

    else:

        return factorial(n-1) * n
