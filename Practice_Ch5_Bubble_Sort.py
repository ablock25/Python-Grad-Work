##One way to sort a list of n different numbers in increasing order
##is to execute n − 1 passes over the numbers in the list.

##Each pass compares all adjacent numbers in the
##list and swaps them if they are out of order.

##At the end of the first pass, the largest item
##will be the last in the list (at index n − 1).

##Therefore, the second pass can stop before reaching the
##last element, as it is already in the right position;

##the second pass will place the second
##largest item in the next to last position.

##In general, pass i will compare pairs at indexes
##0 and 1, 1 and 2, 2 and 3, . . . , and i − 1 and i;

##at the end of the pass, the ith largest item will be at index n − i.

##Therefore, after pass n − 1, the list will be in increasing order.

##Write a function bubbleSort() that takes a list of numbers as input
##and sorts the list using this approach.
## (Perkovic 139)

def bubbleSort(list_nums):

    for i in range(len(list_nums)-1, 0, -1):

        for j in range(i):

            if list_nums[j] > list_nums[j+1]:

                list_nums[j], list_nums[j+1] = list_nums[j+1], list_nums[j]

    print(list_nums)
