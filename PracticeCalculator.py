#User entry- Do you want to add or subtract or multiply or divide?
opUser = input('Do you want to add, subtract, multiply, or divide? : ')
libraryUser1 = ['add', 'Add', 'ADD', '+']
libraryUser2 = ['subtract', 'Subtract', 'SUBTRACT', '-']
libraryUser3 = ['multiply','Multiply','MULTIPLY','*','x','X']
libraryUser4 = ['divide','Divide','DIVIDE','/']
#Ask for 2 numbers one at a time. (Digits 0-9 only, eg. 0 not zero)
userNumber1 = input('Enter a number: ')
userNumber2 = input('Enter a number: ')
userNumber1 = float(userNumber1)
userNumber2 = float(userNumber2)
if opUser in libraryUser1:
    print(userNumber1 + userNumber2)
if opUser in libraryUser2:
    print(userNumber1 - userNumber2)
if opUser in libraryUser3:
    print(userNumber1 * userNumber2)
if opUser in libraryUser4:
    if userNumber2 == 0:
        print("Soorry! *in Canadian accent* can't divide by 0 eh!")

    else:

        print(userNumber1 / userNumber2)
