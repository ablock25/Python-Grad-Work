##Start by setting t to be the local time 1, 500, 000, 000 seconds
##from the start of January 1, 1970 UTC:
## (Perkovic 107)
##>>> import time
##>>> t = time.localtime(1500000000)

import time
t = time.localtime(1500000000)

##Construct the next strings by using the
##string time format function strftime():

##    (a) 'Thursday, July 13 2017'

a = time.strftime('%A, %B %d %Y', t)
print(a)

##    (b) '09:40 PM Central Daylight Time on 07/13/2017'

b = time.strftime('%I:%M %p %Z on %m/%d/%Y', t)
print(b)

##    (c) 'I will meet you on Thu July 13 at 09:40 PM.'

c = time.strftime('I will meet you on %a %B %d at %I:%M %p', t)
print(c)
