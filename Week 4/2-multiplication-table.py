num = int(input('Enter a number: '))

print('\n'.join(f'{num} x {i} = {num*i}' for i in range(1, 11)))

# table_of_num_list = list(f'{num} x {i} = {num*i}' for i in range(1, 11))
# print(table_of_num_list)
# print('\n'.join(table_of_num_list))
