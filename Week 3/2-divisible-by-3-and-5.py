num = int(input('Enter a number: '))
divisible = bool(num%3==0 and num%5==0)
print(f'Is {num} divisible by 3 and 5? {divisible}')