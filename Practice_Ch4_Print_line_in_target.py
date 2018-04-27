##Implement function myGrep():
##that takes as input:
##two strings, a file name and a target string, and prints:
##every line of the file that contains the target string as a substring.

##>>> myGrep('example.txt', 'line')
##The 3 lines in this file end with the new line character.
##There is a blank line above this line.
## (Perkovic 114)

def myGrep(filename, target):
    'prints every line of the file that contains the target string as a substring'

    infile = open(filename)         #open filename and set to variable infile

    for line in infile:         
        if target in line:          #Finds target in each line of filename

            print(line, end=' ')    #prints the line that target appears in and
                                    #moves to next line
