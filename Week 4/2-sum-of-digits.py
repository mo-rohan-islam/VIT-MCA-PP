num = int(input('Enter a number: '))

if num<0:
    print('Invalid input!')
    exit(0)

copy = num
sum = 0

while copy > 0:
    digit = copy % 10
    sum += digit
    copy //= 10

print(f'Sum of digits of {num} is {sum}')