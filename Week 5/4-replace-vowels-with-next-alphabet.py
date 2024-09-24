input_string = input('Enter a string: ')

vowels = 'aeiouAEIOU'
result = input_string

for char in input_string:
    if char in vowels:
        result = result.replace(char, chr(ord(char) + 1))

print(result)