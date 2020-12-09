# FIXME 1: Complete the function. The function takes an ID and returns True or False, based on the ID spec.
# Also, it prints error messages, if the id is invalid
def check_id(id):
    val = [True, True, True]
    slice_object = slice(1, len(id))
    rest_of_id = id[slice_object]
    if len(id) != 9 :
        val[0] = False
        print('The length should be exactly 9 characters long')
    if id[0] != 'C':
        val[1] = False
        print('The ID must begin with the uppercase character "C"')
    # FIXME figure out how to get it to confirm the rest
    # of the ID is all numbers
    if any(c.isalpha() for c in rest_of_id) == True:
        val[2] = False
        print("All characters beside the beginning 'C' character must be numbers")
    
    for check_val in range(len(val)):
        if val[check_val] == False:
            return False
    return True        


if __name__ == "__main__":
    print('This program will check the validity of the student ID at CNU')
    ID_input = str(input('Please enter a student ID or enter q to quit:\n'))
    while ID_input != 'q':
        check_val = check_id(ID_input)
        if check_val == True:
            print('Valid Student ID')
        else:
            print('Invalid student ID')
        ID_input = str(input('Please enter a student ID or enter q to quit:\n'))
    print('Thanks for using the program!')

    