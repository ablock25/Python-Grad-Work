##Write function negatives() that takes a list as input
##and prints, one per line, the negative values in the list.
##The function should not return anything.
## (Perkovic 71)

def negatives(lst):
    for x in lst:
        if x < 0:
            print(x)
