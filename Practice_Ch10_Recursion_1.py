def vertical(n):
    'prints digits of n vertically'

    if n < 10:      ## base case: n has 1 digit 
        print(n)        # just print n

    else:                   # recursive step: n has 2 or more digits
        vertical(n//10)         # recursively return all but last digit
        print(n%10)             # print last digit of n

 
## (Perkovic 333)

## EXAMPLE:

        ## n = 1234
        ## n is not less than 10 so we move onto else statement
        ## vertical(1234//10) = 123
        ## vertical(123//10) = 12
        ## vertical(12//10) == 1
        ## print (1%10) = 1         1ST ROW
        ## print(2%10) = 2          2nd ROW
        ## print(3%10) = 3          3rd ROW
        ## print(4%10) = 4          4th ROW
