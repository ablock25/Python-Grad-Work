##We start by opening the file for reading as a text input stream:

infile = open('example.txt')

##We have multiple string methods that can be used

##infile.read(n)
##Read n characters from the file infile or until the end of the file
##is reached, and return characters read as a string

read_n_char = infile.read(8)
print(read_n_char)
print()

##infile.read()
##Read charactters from file infile until the end of the file and return
##characters read as a string

read_all_file = infile.read()
print(read_all_file)
print()

##infile.readline()
##Read file infile until (and including) the new line character or until
##end of file, whichever is first, and return characters read as a string

read_file_line = infile.readline()
print(read_file_line)
print()

##infile.readlines()
##Read file infile until the end of the file and return the characters
##read as a list lines

read_lines_file = infile.readlines()
print(read_lines_file)
print()

##outfile.write(s)
##Write string s to file outfile

write_outfile = outfile.write(s)
print(write_outfile)

##file.close()
##Close the file
