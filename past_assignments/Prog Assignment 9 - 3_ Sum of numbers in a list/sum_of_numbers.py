# FIXME 1: Complete sum_num. This function takes in a list, and returns the sum of digits in the list
def sum_num(check_list):
    end_sum = 0
    num_list = list()
    for item in check_list:
        if item.isnumeric() == True:
            num_list.append(int(item))
    print(num_list)
    end_sum = sum(num_list)
    return end_sum

if __name__ == "__main__":
    # FIXME 2a:
    print('The sum of all numbers in a list')
    
    # FIXME 2b: Prompt the user to enter list item, separated by a space
    input_list = str(input('Enter list items, separated by a space:\n'))
    entered_list = [str(item) for item in input_list.split()]
    # FIXME 2c: Print the list items as a list
    print(f'The list entered is: {entered_list}')
    
    # FIXME 2d: Call the function sum_num and print the sum.
    sum_up = sum_num(entered_list)
    print(f'The sum of the numbers in the list is: {sum_up}')
    