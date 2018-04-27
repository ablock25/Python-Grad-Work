##Use recursive thinking to implement recursive function cheers()
##that, on integer input n, outputs n strings 'Hip '
##followed by 'Hurray!!! '.
##>>> cheers(0) Hurray!!!
##>>> cheers(1) Hip Hurray!!!
##>>> cheers(4) Hip Hip Hip Hip Hurray!!!
##The base case of the recursion should be when n is 0;
##your function should then print Hurrah.
##When n > 1,your function should print 'Hip ' and then recursively
##call itself on integer input n − 1.
## (Perkovic 334)

def cheers(n):
    '''Prints "hip" n times followed by a final "Hurray!"'''

    if n <= 0:
        print('Hurray!')

    else:
        print('HIP! ', end="")      #If print function put last, then hurray is
        cheers(n-1)                 #printed first instead followed by hips.
