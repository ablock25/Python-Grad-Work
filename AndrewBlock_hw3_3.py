#Andrew Block
#Problem 3

##count_evens():
##This function will accept a list and count the number of even numbers in the list
##and return that value.

##So count_evens(numbers) would return 16.

numbers = [76, 93,  3, 35, 30, 74,  8, 27, 19, 96, 33, 16, 16, 56, 98, 28, 19, 14, 63, 53,  2, 60,  4, 93, 61, 3, 56, 31, 25, 74]

def count_evens(numbers):
    'Counts the number of even numbers in a given list'
    count = 0
    for number in numbers:
        if number%2 == 0:
            count = count + 1
    return count
