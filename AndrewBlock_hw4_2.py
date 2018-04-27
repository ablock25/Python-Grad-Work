###Andrew Block
###Problem 2

##Write a function that takes as its input a filename, and an integer.

def line_transfer(filename, number_lines):
    
    '''Takes the first number of lines given by the second argument
    from the file specified in the first argument, and outputs the
    specified lines to a new file called output_log.txt
    '''
    
##open the files incuding exception handling.

    try:
        infile = open(filename, 'r')
        outfile = open('output_log.txt', 'w')

    except FileNotFoundError:
        print('Sorry, was unable to open that file')
        return
        
##Read in the first number of lines given as the second argument.  

    counter = 0
          
    for counter in range(number_lines):
        content = infile.readline()
        outfile.write(content)  #Write content to outfile = output_log.txt
        counter += 1    #  counter += 1 == counter = counter + 1

##Close both files
        
    infile.close()
    outfile.close()

