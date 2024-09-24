# Read a string and display the count of alphabets and digits in it

def main():
    # Take input
    input_string = input('Enter an alphanumric string: ')

    count_dict = count_with_regex(input_string)
    # count_dict = count_without_regex(input_string)

    print(f'\nInput String: {input_string}\n')
    print_count(count_dict)


# Alphabet and Digit counters
def count_with_regex(input_string):
    from re import findall

    alpha_count = len(findall(r'[a-zA-Z]', input_string))
    digit_count = len(findall(r'[0-9]', input_string))
    other_count = len(findall(r'[^a-zA-Z0-9]', input_string))

    count_dict = dict(
        alphas = alpha_count,
        digits = digit_count,
        others = other_count
    )

    return count_dict


def count_without_regex(input_string):
    alpha_count = 0
    digit_count = 0
    other_count = 0

    # Loop through each character of the input
    for character in input_string:
        if character.isalpha():
            alpha_count += 1
        elif character.isdigit():
            digit_count += 1
        else:
            other_count += 1
    
    count_dict = dict(
        alphas = alpha_count,
        digits = digit_count,
        others = other_count
    )

    return count_dict


def print_count(count_dict):
    alphas = 'alphas'
    digits = 'digits'
    others = 'others'

    # Display the counts
    print(f'Alphabet count: {count_dict.get(alphas)}')
    print(f'Digit count: {count_dict.get(digits)}')
    print(f'Others count: {count_dict.get(others)}')


if __name__ == '__main__':
    main()