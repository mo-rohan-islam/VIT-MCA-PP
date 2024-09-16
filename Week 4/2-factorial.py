def main():
    # Input
    num = int(input('Enter a number: '))

    # Check for invalid input
    if num<=0:
        print('Invalid input!\nEnter a value greater than 0.')
        exit(0)

    # Calculate factorial
    factorial = factorial_with_recursion(num)
    # factorial = factorial_with_for(num)
    # factorial = factorial_with_while(num)

    # Print factorial
    print(f'The factorial of {num} is {factorial}.')

def factorial_with_while(num):
    i = 1
    factorial = 1
    while i<=num:
        factorial *= i
        i += 1
    return factorial

def factorial_with_for(num):
    factorial = 1
    for num in range(1,num+1):
        factorial *= num
    return factorial

def factorial_with_recursion(num):
    if num == 1:
        return 1
    return num * factorial_with_recursion(num-1)

if __name__ == '__main__':
    main()
