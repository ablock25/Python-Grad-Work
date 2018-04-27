##Write a function interest() that takes one input,
##a floating-point interest rate
##(e.g., 0.06 which corresponds to a 6% interest rate).
##Your function should compute and return how long (in years)
##it will take for an investment to double in value.
##Note: The number of years it takes for an investment
##to double does not depend on the value of the initial investment.
## (Perkovic 144)

def interest(RateofInvestment):

    'Returns number of years until investment is doubled'
    
    Investment = 1000
    Counter = 0

    while Investment < 2000:
        Investment += Investment * RateofInvestment
        Counter += 1

    print(Counter)
