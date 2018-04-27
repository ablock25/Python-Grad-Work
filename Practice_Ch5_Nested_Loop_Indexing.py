##Write a function add2D() that takes two two-dimensional lists of same size
##(i.e., same number of rows and columns) as input arguments
##and increments every entry in the first list with
##the value of the corresponding entry in the second list.

##Practice Problem 5.9

##>>> t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
##>>> s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
##>>> add2D(t,s)
##>>> for row in t:
##    print(row)
##[4, 8, 4, 5]
##[5, 2, 10, 3]
##[8, 4, 6, 6]
# (Perkovic 143)

def add2D(lst1,lst2):
    'Takes 2 two dimensional lists and adds their corresponding columns'
    
    num_rows = len(lst1)    # number of rows in list 1
    num_col = len(lst1[0])  # number of columns in list 1


#Takes first number in the first column/row and adds to list 2.
    #Iterates back to 2nd column of the first row and repeats until done

    for row in range(num_rows):             
        for i in range(num_col):
            nums = lst1[row][i] + lst2[row][i]
            print(nums, end=' ')
        print()
