#Andrew Block
#Problem 1
#Create an empty list
listNumbers = []
#Ask user to enter 3 numbers, one at a time entered into empty list
n1 = input('Enter number: ')
n2 = input('Enter number: ')
n3 = input('Enter number: ')
#Append to add values into list
listNumbers.append(int(n1))
listNumbers.append(int(n2))
listNumbers.append(int(n3))
#Output highest
highestNumber = max(listNumbers)
print('The highest number is: ', highestNumber)
#Output lowest
lowestNumber = min(listNumbers)
print('The lowest number is: ', lowestNumber)
#Output average(round to 1 decimal) number in the list
averageNumber = sum(listNumbers)/3
print('The average is: ', round(averageNumber,1))
