'''
This module provides the capability to check whether a given number is prime or not
'''
from math import isqrt

def main():
    num = int(input('Enter a number: '))

    if num <=1:
        print('Invalid input!')
        exit(0)

    if isPrime(num):
        print(f'{num} is a Prime Number.')
    else:
        print(f'{num} is not a Prime Number.')


def isPrime(num):
    '''
    Returns True if a number is Prime otherwise returns False
    '''
    for i in range(2, isqrt(num)+1):
        # print(i)
        if num%i==0:
            return False
    else:
        return True


if __name__ == '__main__':
    main()