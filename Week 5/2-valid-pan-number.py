# Check whether the input is a valid PAN

# Take input
input = input('Enter a PAN number: ')

## Validation
# Length of 10 chars
length_check = len(input)

# First 5 letters alphabets
alphabet_check = input[:5].isalpha()

# 6th to 9th position is digit
digit_check = input[5:9].isdigit()

# Last position is alphabet
last_position_check = input[-1].isalpha()

# If all checks hold true then valid PAN else invalid
if length_check and alphabet_check and digit_check and last_position_check:
    print('Valid PAN')
else:
    print('Invalid PAN')