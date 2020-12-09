# FIXME 1: Complete create_list function. It has no parameters, and it returns a list of the weights.
# Note: Prompt the user to enter four numbers, each corresponding to a person's weight in pounds.
def create_list():
    weight_list = []
    # Finish it
    i = 0
    while i <= 3:
        weight_list.append(float(input(f'Enter weight {i + 1}:\n')))
        i += 1
    return weight_list
#FIXME 2: Complete average_weight function. This function takes in a list of weights and returns the average.
# Note: no print
def average_weight(list_items):
    sum_nums = sum(list_items)
    ave = sum_nums / len(list_items)
    return ave
#FIXME 3: This finction takes in weight in pound (float), and returns weight in kilogram (float)
def pound_to_kilo(pound):
    kilo = pound / 2.2
    return kilo

if __name__ == "__main__":
    pass
    #FIXME 4a: Print a statement that says the program's name "People's weights"
    print('People\'s weights')
    
    #FIXME 4b: Call the create_list function to get the weights and put them in a list. Then print the list.
    created_list = create_list()
    print(created_list)

    #FIXME 4c: Call average_weight, and Output the average of the list's items with two digits after the decimal point.
    avg_weight = average_weight(created_list)
    print(f'Average Weight: {avg_weight}')

    # FIXME 4d: Output max weight from list.
    max_weight = max(created_list)
    print(f'Max Weight is: {max_weight}')
    
    # FIXME 4e: Prompt the user for a list index and output that weight in pounds and kilograms.
    # Note: call pound_to_kilo function
    choice = int(input('Enter which weight you want converted to kilograms (1, 2, 3, or 4): ')) - 1
    kilograms = pound_to_kilo(created_list[choice])
    print(f'the kilogram conversion for weight {created_list[choice]} is {kilograms}')

    # FIXME 4f: Sort the list and output it.
    print(f'The list sorted is {created_list.sort()}')
    