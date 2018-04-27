##Write a function xmult() that takes two lists of integers as input
##and returns a list containing all products of integers
##from the first list with the integers from the second list.
##>>> xmult([2], [1, 5]) [2, 10]
##>>> xmult([2, 3], [1, 5]) [2, 10, 3, 15]
##>>> xmult([3, 4, 1], [2, 0]) [6, 0, 8, 0, 2, 0]
## (Perkovic 138)

def xmult(list1,list2):

    new_list = []
    
    for x in list1:

        for y in list2:
            number = x * y
            new_list.append(number)
            
    print(new_list)
