#Formatted list

for i in range(1,13):
	formatted_list = '{0:3}{1:6}{2:6}{3:6}'.format(i, i**2, i**3, 2**i, sep='	')
	print(formatted_list)

def growthrates(n):
        'prints values of below 3 functions for i = 1, ..., n'
        print(' i	i**2	i**3	2**i')
        formatStr = '{0:2d} {1:6d} {2:6d} {3:6d}'
        for i in range(2, n+1):
                print(formatStr.format(i, i**2, i**3, 2**i))
# (Perkovic 105)
