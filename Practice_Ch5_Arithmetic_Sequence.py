##Write function arithmetic() that takes a list of integers as input
##and returns True if they form an arithmetic sequence.
##(A sequence of integers is an arithmetic sequence if the difference
## between consecutive items of the list is always the same.)
##>>> arithmetic([3, 6, 9, 12, 15]) True
##>>> arithmetic([3, 6, 9, 11, 14]) False
##>>> arithmetic([3]) True
## (Perkovic 134)

def arithmetic(lst_sequence):
    'Checks to see if the list is arranged in an arithmetic sequence'

    #Need to account for single element list
    if len(lst_sequence) < 2:
        print('''A one element list is technically an arithmetic sequence.
are you sure you don't want to check a longer list?''')
        return True
        
        #Must first check the first two elements to get benchmark
    diff = lst_sequence[1] - lst_sequence[0]
    
    for i in range(1, len(lst_sequence) - 1):
        if lst_sequence[i+1] - lst_sequence[i] != diff:
            return False

    #If the loop does not find a false value, the print statement will be returned
    print('The list is an arithmetic progression')
