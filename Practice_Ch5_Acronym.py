##An acronym is a word formed by taking the first letters of the words
##in a phrase and then making a word from them.
##For example, RAM is an acronym for random access memory.

##Write a function acronym() that takes a phrase (i.e., a string) as input
##and then returns the acronym for that phrase.

##Note: The acronym should be all uppercase,
##even if the words in the phrase are not capitalized.
## (Perkovic 136)

def acronym(phrase):
    'Retrieves the acronym for the entered phrase'

    #First we need to break the string into a list we can iterate over

    words_list = phrase.split()

    Acro = ''
    for word in words_list:
        Acro += word[0].upper()

    print(Acro)
