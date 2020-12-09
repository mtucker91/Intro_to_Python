# FIXME 1: Complete the function. This function takes a string, and returns boolean (True or False)
# True: when all char in the string are 0 or 1; False, otherwise.
def check_binary(str):
    for index in range(len(str)):
        if(str[index] == '0' or str[index] == '1'):
            ret_val = True
        else:
            return False
    return ret_val
if __name__ == "__main__":
    #FIXME 2a: Print a statement that says what the program is going to do.
    print('This program is going to check if an entered string is binary or not')
    # FIXME 2b: Prompt the user to enter a string
    string_input = str(input('Enter a string:\n'))
    # FIXME 2c: Call the function to check the string, then print the result
    binary_check = check_binary(string_input)
    if binary_check == True:
        print(f'{string_input} is binary')
    else:
        print(f'{string_input} is not binary')
    # FIXME 2d: Print Done! at the end
    print('Done!')
    