##Translate these conditional statements into Python if statements: (
##a) If age is greater 62, print 'You can get your pension benefits'.
##(b) If name is in list ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'],
##print 'One of the top 5 baseball players, ever!'.
##(c) If hits is greater than 10 and shield is 0, print 'You are dead...'.
##(d) If at least one of the Boolean variables north, south, east, and west
##is True, print 'I can escape.'.
a = eval(input('Enter your age: '))

if a > 62:
    print('You can get your pension benefits')

lst_b = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
b = input("Enter your favorite baseball player's last name: ")

if b in lst_b:
    print('One of the top 5 baseball players ever!')

hits = eval(input('How many times have you been hit? '))
shield = eval(input('How much shield do you have left? '))

if hits > 10 and shield == 0:
    print('You are dead')

d = input('what cardinal direction is out? ')

if d in ['south','east','west','north']:
    print('I can escape!')
