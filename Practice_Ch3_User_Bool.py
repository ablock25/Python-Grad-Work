#Implement function noVowel() that takes a string s as input
#and returns True if no character in s is a vowel,
#and False otherwise (i.e., some character in s is a vowel).
# (Perkovic 69)

#We need to use a for loop to check whether or not each character
#of the input string is a vowel. If yes, we can return False immediately.
#We can return True only after all the characters have been checked,
#that is, when the for loop has completed execution.

def noVowel(s):
    for c in s:
        if c in 'aeiouAEIOU':
            return False
    return True
# (Perkovic 83)
