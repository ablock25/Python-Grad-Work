##Assuming that variable forecast has been assigned string
##'It will be a sunny day today'

forecast = 'It will be a sunny day today'

##write Python statements corresponding to these assignments:

##(a) To variable count, the number of occurrences of string
##'day' in string forecast.

count = forecast.count('day')
print(count)
print()

##(b) To variable weather, the index where substring 'sunny' starts.

weather = forecast.find('sunny')
print (weather)
print()

##(c) To variable change, a copy of forecast in which
##every occurrence of substring 'sunny' is replaced by 'cloudy'.

change = forecast.replace('sunny','cloudy')
print(change)
print()

## (Perkovic 98)
