# Check whether a given string is palindrome or not

def main():
    input_string = input('Enter a string: ')
    reverse_string = input_string[::-1]

    palindrome_check_by_char_compare(input_string, reverse_string)
    # palindrome_check(input_string, reverse_string)


def palindrome_check(input_string, reverse_string):
    if input_string.lower() == reverse_string.lower():
        print(f'{input_string} is a Palindrome')
    else:
        print(f'{input_string} is not a Palindrome')


def palindrome_check_by_char_compare(input_string, reverse_string):
    for char_in, char_rev in zip(input_string.casefold(), reverse_string.casefold()):
        if char_in != char_rev:
            print(f'{input_string} is not a Palindrome')
            break
    else:
        print(f'{input_string} is a Palindrome')


if __name__ == '__main__':
    main()