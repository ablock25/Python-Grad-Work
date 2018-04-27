#Implement a program that requests from the user
#a list of words (i.e., strings)
#and then prints on the screen, one per line,
#all four-letter strings in the list.
# (Perkovic 65)
word_list = []
word_1 = word_list.append(input('enter a word: '))
word_2 = word_list.append(input('enter a word: '))
word_3 = word_list.append(input('enter a word: '))
word_4 = word_list.append(input('enter a word: '))
word_5 = word_list.append(input('enter a word: '))

for word in word_list:
    if len(word) == 4:
        print(word)
