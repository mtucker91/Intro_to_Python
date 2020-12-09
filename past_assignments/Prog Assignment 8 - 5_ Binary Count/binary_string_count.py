# FIXME 1: Complete the function. This function takes a string, and returns boolean (True or False)
# True: when all char in the string are 0 or 1; False, otherwise.
def check_binary(str):
    for index in range(len(str)):
        if(str[index] == '0' or str[index] == '1'):
            ret_val = True
        else:
            print(f'{string_input} is not binary')
            return False
    print(f'{string_input} is binary')
    return ret_val

# FIXME 2: Complete the function. This function takes a BINARY and returns the count of 0s and 1s, as a tuple.
def binary_count(binary_str):
    count0 = 0
    count1 = 0

    for index in range(len(binary_str)):
        if binary_str[index] == '0':
            count0 += 1
        elif binary_str[index] == '1':
            count1 += 1
    return count0, count1

if __name__ == "__main__":
    #FIXME 3a: Print a statement that says what the program is going to do.
    print("Counting the number of 0's and 1's in a binary string")
    # FIXME 3b: The program should run as long as the user wants.
    contin = 'y'
    counts = []
    while contin == 'y':
        # FIXME 3c: Prompt the user to enter a string
        string_input = str(input('Enter a string:\n'))
        # FIXME 3d: Call the function check_binary to check the string binary,
        if check_binary(string_input) == True:
        # If binary, call the function binary_count to print the result.
            counts = binary_count(string_input)
            print(f'Number of 0s is {counts[0]}')
            print(f'Number of 1s is {counts[1]}')
        contin = str(input('Would you like to enter another statement (y or n):\n'))
    # FIXME 2e: Print Done! at the end
    print('Done!')