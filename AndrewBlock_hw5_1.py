##Andrew Block
##Problem 1

def creditCardCount(Transaction_File):
    '''Asks for the type of card to search for and returns the # of times used
    from the given transaction file.'''

##The file will be 'transactions.csv' for this example.

    try:    
        transactions = open(Transaction_File,'r')   

    except IOError or FileNotFoundError:
        print('Unable to find file')

        return -1
##User enters a # 1-3 and the string is cast to an int.
    cardName = int(input('''Which card would you like to search for?
    1=Visa
    2=American Express
    3=Mastercard
Enter 1-3:  '''))       

#Counter initialized to 0 outside loop.
    count = 0

#Each string is cast to a list, and each list is given a conditional statement.
#If the conditional statement is satisfied, then 1 is added to the counter.
    for transaction in transactions:    
        transaction = transaction.split(',')
    
        if cardName == 1:
            if transaction[3] == 'Visa':
                count = count + 1
        elif cardName == 2:
            if transaction[3] == 'Amex':
                count = count + 1
        elif cardName == 3:
            if transaction[3] == 'Mastercard':
                count = count + 1

    transactions.close()
    print('There are {} transactions that used this card.'.format(count))
    
creditCardCount('transactions.csv')
