def main():
    input_string = input('Enter a string: ')
    substring = input('Enter a substring: ')

    # substring_count = find_substring_with_inbuilt_method(input_string, substring)
    substring_count = find_substring_inhouse(input_string, substring)
    # substring_count = input_string.count(substring)     # Forgot about it

    print(f'\nThe count of substring \'{substring}\' in input string \'{input_string}\' is {substring_count}.')


'''
index = 0
while index <= length of input - length of substring   
    position = 0
    while position < length of substring        0,4 | 5 | 4 < 5
        if substring[pos] == input[index + pos]
            position + 1
        else
            break
    else
        found = True
        Match found at index
    index + position + 1       0, 4 | 0 + 4 = 4 + 1 

if not found 
    Not found
'''

def find_substring_inhouse(input_string, substring):
    length_of_string = len(input_string)
    length_of_substring = len(substring)
    index = 0
    substring_counter = 0

    while index <= length_of_string - length_of_substring:
        position = 0
        while position < length_of_substring:
            if substring[position].casefold() == input_string[index + position].casefold():
                position += 1
            else:
                break
        else:
            substring_counter += 1
            print(f'Substring \'{substring}\' found at position: {index}')
        index += position + 1
    
    if substring_counter == 0:
        print(f'Substring \'{substring}\' not found in input string \'{input_string}\'')
    
    return substring_counter


def find_substring_with_inbuilt_method(input_string, substring):
    length_of_string = len(input_string)
    length_of_substring = len(substring)
    index = 0
    substring_counter = 0

    while index < length_of_string - length_of_substring:       # len 5 | len 20 == 0,4 | 0,19  ||  20-5 = 15 | 15: = 15,16,17,18,19
        position = input_string.find(substring, index)
        if position != -1:
            substring_counter += 1
            print(f'Substring \'{substring}\' found at position: {position}')
            index = position + length_of_substring
        else:
            break

    if substring_counter == 0:
        print(f'Substring \'{substring}\' not found in input string \'{input_string}\'')

    return substring_counter


if __name__ == '__main__':
    main()