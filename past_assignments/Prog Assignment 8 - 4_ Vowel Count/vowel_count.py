# FIXME 1: Complete the function. The function take a string, and returns the number of vowels in the string
# Hint: check every char in the string if it is a vowel or not.
def vowel_count(str):
    i = 0
    vowels = set('aeiou')
    str = str.lower()
    for index in range(len(str)):
        for c in vowels:
            if c == str[index]:
                i += 1
    return i
if __name__ == "__main__":
    # FIXME 2a: Print a statement that says what the program is going to do.
    print('This program counts the number of vowels in a statement')
    # FIXME 2b: The program should run as long as the user wants.
    contin = 'y'
    while contin == 'y':
        # FIXME 2c: Prompt the user to enter a statement
        string_input = str(input('Enter a statement:\n'))

        # FIXME 2d: Call the function vowel_count and print the result
        count_vowels = vowel_count(string_input)
        print(f'The number of vowels in "{string_input}" is {count_vowels}')
        contin = str(input('Would you like to enter another statement (y or n):\n'))

    # FIXME 2e: Print Thank you! message when the user is done.
    print('Thank You!')
