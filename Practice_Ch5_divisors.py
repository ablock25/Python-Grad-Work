##Write function divisors() that takes a positive integer n as input
##and returns the list of all positive divisors of n.
##>>> divisors(1) [1]
##>>> divisors(6) [1, 2, 3, 6]
##>>> divisors(11) [1, 11]
## (Perkovic 137)

def divisors(number):

    new_list = []

    for n in range(1, number +1):
        if number % n == 0:
            new_list.append(n)

    print(new_list)
