password = input('Enter your password: ')

length_check = len(password) >= 8
upper_check = False
lower_check = False
number_check = False

for char in password:
    if not upper_check:
        upper_check = char.isupper()
    if not lower_check:
        lower_check = char.islower()
    if not number_check:
        number_check = char.isdigit()
    if upper_check and lower_check and number_check:
        print('Valid Password!')
        break
else:
    print('\nPassword does not meet the requirements!')
    print(f'\nHas Length > 8 characters: {length_check}')
    print(f'Has 1 Upper case character: {upper_check}')
    print(f'Has 1 Lower case character: {lower_check}')
    print(f'Has 1 Digit: {number_check}')