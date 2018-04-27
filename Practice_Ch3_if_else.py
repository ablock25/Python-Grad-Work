##Translate these into Python if/else statements:
##(a) If year is divisible by 4, print 'Could be a leap year.';
##otherwise print 'Definitely not a leap year.'
##(b) If list ticket is equal to list lottery, print 'You won!';
##else print 'Better luck next time...'
## (Perkovic 62)

Year = eval(input("What year is it? "))

if Year % 4 == 0:
    print("Could be a leap year!!")
else:
    print("Definitely not a leap year!!")

list_ticket = (input('what were your 5 lottery numbers? '))
list_lottery = '12345'
if list_ticket == list_lottery:
    print('You won!')
else:
    print('Better luck next time champ')
