##Implement function rlookup() that provides
##the reverse lookup feature of a phone book.

##Your function takes, as input, a dictionary representing a phone book.
##In the dictionary, phone numbers (keys) are mapped to individuals (values).

##Your function should provide a simple user interface
##through which a user can enter a phone number and obtain
##the first and last name of the individual assigned that number.

##(Perkovic 170)

def rlookup():

    '''Reverse phone lookup up with short dictionary,
    returns the name attached to the entered phone number.
    The program is also in an infinite loop for repeat subscribers.'''
    
    rphonebook = {
        '(123)456-7890':['Anna','Karenina'],
        '(901)234-5678':['Yu', 'Tsun'],
        '(321)908-7654':['Hans', 'Castorp'],
        '(440)382-6611':['Shnosey', 'Me'],
        '(440)420-6559':['Shnosey', 'Ju']}

    try:
        while True:
        
            person = input('''Enter phone number in the format (xxx)xxx-xxxx
or press CTRL-C to exit: ''')
            if person in rphonebook:
                print(rphonebook[person])

            else:
                print('phone not in use')
    except:
        print('Thank you for using our service! See you next time!')

