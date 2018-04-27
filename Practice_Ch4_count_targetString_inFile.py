##Write function stringCount() that takes two string inputs
##—a file name and a target string— and returns the number of occurrences
##of the target string in the file.
##>>> stringCount('example.txt', 'line') 4

def stringCount(filename, target):
    'Prints the # of occurences of target in the file name'
    infile = open(filename)
    content = infile.read()
    infile.close()
    return content.count(target)

def numWords(filename):
    'prints a list of words from file and returns the length of the list'
    infile = open(filename)
    content = infile.read()
    infile.close()

    wordList = content.split()
    print(wordList)
    return len(wordList)

##Write function words() that
##takes one input argument—a file name—and
##returns the list of actual words (without punctuation symbols !,.:;?)
##in the file.
##>>> words('example.txt')
##['The', '3', 'lines', 'in', 'this', 'file', 'end', 'with',
##'the', 'new', 'line', 'character', 'There', 'is', 'a',
##'blank', 'line', 'above', 'this', 'line']

def words(filename):
    'Prints list of words without punctuation'
    infile = open(filename)
    content = infile.read()
    infile.close()

    table = str.maketrans('!,.?:;', '      ') #Make a translation table
    
    content = content.translate(table) #translate content using translation table

    content = content.lower() #make everything in contect lowercase

    return content.split() # split the string into a list and return the list

def numLines(filename):
	infile = open(filename)
	lineList = infile.readlines()
	infile.close()
	
	print(lineList)
	return len(lineList)
