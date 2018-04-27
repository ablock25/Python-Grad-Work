##Implement a program that starts by asking the user to enter a login id (i.e., a string).
##The program then checks whether the id entered by the user is in the list:
##['joe', 'sue', 'hani', 'sophie'] of valid users.
##Depending on the outcome, an appropriate message should be printed.
##Regardless of the outcome, your function should print 'Done.'
##before terminating. 
## (Perkovic 62)

valid_users = ['joe', 'sue', 'hani', 'sophie']
user_id = input('Login: ')

if user_id in valid_users:
    print('You have succesfully logged in')
else:
    print('Login error, please try again. ')
print('Done')
