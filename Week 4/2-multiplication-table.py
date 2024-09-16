num = int(input('Enter a number: '))

print('\n'.join(f'{num} x {i} = {num*i}' for i in range(1, 11)))
# print(list(f'{num} x {i} = {num*i}' for i in range(1, 11)))
