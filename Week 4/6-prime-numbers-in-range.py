from importlib import import_module
# from prime import isPrime

# Standard import [from prime import isPrime] could not be used as file name does not start with letter or underscore
# prime = __import__('2-prime')         # __import__ is for internal use by Python and is not recommended    
prime = import_module('2-prime')        # import prime      -- except that Python interpreter does not allow module name to start with number

limit = int(input('Check for Primes until: '))

if limit<=1:
    print('Invalid input! Limit should be greater than 1')
    exit(0)

for num in range(2, limit+1):
    # check for prime and print
    # if isPrime(num):      # from prime import isPrime
    if prime.isPrime(num):
        print(num, end=', ')
