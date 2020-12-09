# FIXME 1: Complete the not_in_list function.
# This function takes an int and a list, and return True if int is not in the list or False otherwise
def not_in_list(num, my_list):
    retval = True
    for number in my_list:
        if num == number:
            return False
        else:
            retval = True
    return retval

# FIXME 2:  Complete the print_list function.
# This function takes a list, and print the contents of the list. No return
def print_list(my_list):
    print('The contents of the list are:')
    for number in my_list:
        print(number)

# ******************** START PROGRAM HERE ******************************
if __name__ == "__main__": 
    my_list = [] # initialize array
    count = 0 # initialize increment counter
    # FIXME 3-a: print instruction statement
    print('This program will prompt the user to enter 6 different numbers in a list')

    # FIXME 3-b: Prompt the user to input 6 different numbers, all int. Use a while loop
    while count <= 5: #loop for as long as we don't get to 6 numbers (remember count starts at 0 so <= 5 is considered correct)
        num_input = int(input('Please enter a number:\n'))
    # FIXME 3-c: Read the input number, test if it is already in the list (call `not_in_list function`),
    # and add it to the list if it is not (use append function)
        checking = not_in_list(num_input, my_list)
        if checking == True:
            my_list.append(num_input)
        else:
            count -= 1 #since the end of the loop auto-increments at the end, we want to decrement once so we "stay in the same place" to ask for a replacement number
            print('The number', num_input, 'is already in the list!')
        count += 1

    # FIXME 3-d: Call the print_list function
    print_list(my_list) #call the function to complete the rest of the program.


