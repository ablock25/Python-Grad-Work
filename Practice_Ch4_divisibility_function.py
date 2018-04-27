##Write function even() that takes a positive integer n as input
##and prints on the screen all numbers between, and including, 2 and n
##divisible by 2 or by 3, using this output format:
##
##>>> even(17) 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16,
## (Perkovic 100)

def even(n):
    'take input (n) and find all numbers between 2 and n that are divisible by 2 or 3'
    for x in range(2, n+1):
        if x%2 == 0 or x%3 == 0:
            print(x, end=', ')
