def numChars(filename):
    'returns the number of characters in file filename'
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    return len(content)
