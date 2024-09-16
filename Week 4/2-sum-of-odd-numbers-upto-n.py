# 1 + 3 + 5 + 7 + N

N = int(input('Enter a number: '))
sum = 0
for num in range(1, N+1, 2):
    print(f'{num} + ', end='')
    sum += num
print(f'\nThe sum is {sum}')