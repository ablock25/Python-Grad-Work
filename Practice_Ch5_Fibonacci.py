##FIBONACCI SEQUENCE

def fibonacci(bound):
    'returns the smallest Fibonacci number greater than bound'

    previous = 1	# first Fibonacci number current = 1
    current = 1         # second Fibonacci number

    while current <= bound:

# current becomes previous, and new current is computed
        previous, current = current, previous+current

    return current

## (Perkovic 146)
