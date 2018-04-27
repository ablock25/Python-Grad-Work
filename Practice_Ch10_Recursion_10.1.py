##Implement recursive method reverse() that takes
##a nonnegative integer as input and prints its digits vertically,
##starting with the low-order digit.
##>>> reverse(3124)
##4
##2
##1
##3
##Let’s summarize the process of solving a problem recursively:
##
##    1. First decide on the base case or cases of the problem
##    that can be solved directly, without recursion.
##
##    2. Figure out how to break the problem into one or more subproblems that
##    are closer to the base case; the subproblems are to be solved recursively.
##
##    The solutions to the subproblems are used to construct the solution
##    to the original problem.
## (Perkovic 334)

def reverse(n):
    '''Takes a nonnegative integer and prints its digits vertically
starting at the ending digit'''

    #BASE CASE: if int is <10: print(int)
    if n < 10:
        print(n)

    else:
        print(n%10)
        reverse(n//10)
